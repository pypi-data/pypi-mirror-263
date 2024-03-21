import os
import sys
import numpy as np
import functools

import siren
from siren import _util
from siren.LIController import LIController

import DarkNews

@functools.wraps(LIController.GenerateEvents)
def GenerateEvents(self, N=None):
    if N is None:
        N = self.events_to_inject
    count = 0
    while (self.injector.InjectedEvents() < self.events_to_inject) and (count < N):
        print("Injecting Event", count)
        tree = self.injector.GenerateEvent()
        print("Weighting Event", count)
        self.weighter.EventWeight(tree)
        print("Done weighting Event", count)
        print()
        self.events.append(tree)
        count += 1
    #if hasattr(self, "DN_processes"):
    #    self.DN_processes.SaveCrossSectionTables()
    return self.events

LIController.GenerateEvents = GenerateEvents

darknews_version = _util.normalize_version(DarkNews.__version__)

resources_dir = _util.resource_package_dir()

# Define a DarkNews model
model_kwargs = {
    "m4": 0.02,
    "mu_tr_mu4": 2.5e-6,  # 1e-6, # GeV^-1
    "UD4": 0,
    "Umu4": 0,
    "epsilon": 0.0,
    "gD": 0.0,
    "decay_product": "photon",
    "noHC": True,
    "HNLtype": "dirac",
}

# Number of events to inject
events_to_inject = 1000

# Expeirment to run
experiment = "CCM"

# Define the controller
controller = LIController(events_to_inject, experiment)

# Particle to inject
primary_type = siren.dataclasses.Particle.ParticleType.NuMu

xs_path = _util.get_cross_section_model_path(f"DarkNewsTables-v{darknews_version}", must_exist=False)
# Define DarkNews Model
table_dir = os.path.join(
    xs_path,
    "Dipole_M%2.2f_mu%2.2e" % (model_kwargs["m4"], model_kwargs["mu_tr_mu4"]),
)
controller.InputDarkNewsModel(primary_type, table_dir, model_kwargs)

# Primary distributions
primary_injection_distributions = {}
primary_physical_distributions = {}

# energy distribution
nu_energy = 0.02965  # from pi+ DAR
edist = siren.distributions.Monoenergetic(nu_energy)
primary_injection_distributions["energy"] = edist
primary_physical_distributions["energy"] = edist

# Flux normalization:
# using the number quoted in 2105.14020, 4.74e9 nu/m^2/s / (6.2e14 POT/s) * 4*pi*20m^2 to get nu/POT
flux_units = siren.distributions.NormalizationConstant(3.76e-2)
primary_physical_distributions["flux_units"] = flux_units

# direction distribution: cone from lower W target
opening_angle = np.arctan(12 / 23.0)
# slightly larger than CCM
lower_target_origin = siren.math.Vector3D(0, 0, -0.241)
detector_origin = siren.math.Vector3D(23, 0, -0.65)
lower_dir = detector_origin - lower_target_origin
lower_dir.normalize()
lower_inj_ddist = siren.distributions.Cone(lower_dir, opening_angle)
phys_ddist = (
    siren.distributions.IsotropicDirection()
)  # truly we are isotropicprimary_injection_distributions['direction'] = direction_distribution
primary_injection_distributions["direction"] = lower_inj_ddist
primary_physical_distributions["direction"] = phys_ddist

# Position distribution: consider neutrinos from a point source
max_dist = 25
lower_pos_dist = siren.distributions.PointSourcePositionDistribution(
    lower_target_origin - detector_origin, max_dist, set(controller.GetDetectorModelTargets()[0])
)
primary_injection_distributions["position"] = lower_pos_dist

# SetProcesses
controller.SetProcesses(
    primary_type, primary_injection_distributions, primary_physical_distributions
)

controller.Initialize()

def stop(datum, i):
    secondary_type = datum.record.signature.secondary_types[i]
    return secondary_type != siren.dataclasses.Particle.ParticleType.N4

controller.injector.SetStoppingCondition(stop)

events = controller.GenerateEvents()

controller.SaveEvents(
    "output/CCM_Dipole_M%2.2f_mu%2.2e_example.hdf5"
    % (model_kwargs["m4"], model_kwargs["mu_tr_mu4"])
)
