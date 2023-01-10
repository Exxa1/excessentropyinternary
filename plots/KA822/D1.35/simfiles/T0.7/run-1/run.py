#!/usr/bin/python3
#                               
#PBS -v PYTHONPATH

import sys, os                              

# if running as batch job need to explicitly change to the correct directory
if 'PBS_O_WORKDIR' in os.environ:
    workingDir = os.environ["PBS_O_WORKDIR"]
    os.chdir(workingDir)		

import rumd
from rumd.Simulation import Simulation
	    
# create simulation object
sim = Simulation("start.xyz.gz")
      
# create integrator object
itg = rumd.IntegratorNVT(targetTemperature=0.7, timeStep=0.005)
sim.SetIntegrator(itg)
	    
# create potential object
pot = rumd.Pot_LJ_12_6_smooth_2_4(cutoff_method = rumd.ShiftedPotential)
pot.SetParams(i=0, j=0, Epsilon=1.00, Sigma=1.00, Rcut=2.5)
pot.SetParams(i=0, j=1, Epsilon=1.50, Sigma=0.80, Rcut=2.5)
pot.SetParams(i=0, j=2, Epsilon=1.25, Sigma=0.90, Rcut=2.5)
pot.SetParams(i=1, j=1, Epsilon=0.50, Sigma=0.88, Rcut=2.5)
pot.SetParams(i=1, j=2, Epsilon=1.00, Sigma=0.84, Rcut=2.5)
pot.SetParams(i=2, j=2, Epsilon=0.75, Sigma=0.94, Rcut=2.5)
sim.SetPotential(pot)

from rumd.Autotune import Autotune
at = Autotune()
at.Tune(sim)

nStepsPrBlock = 2**18
nBlocks = 150
nSteps = nBlocks*nStepsPrBlock 
sim.SetBlockSize(nStepsPrBlock)
sim.Run(nSteps)
	    
sim.WriteConf("end.xyz.gz")

