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
import rumd.Tools

# define temp
T = 5.5
# define new density you want
new_rho = 1.2
	    
# create simulation object
sim = Simulation("start.xyz.gz")

# can define as function if wanted, but then you have to call it.
# def SetDensity(sim, new_rho):

# scale to get right density
nParticles = sim.GetNumberOfParticles()
vol = sim.GetVolume()
currentDensity = nParticles/vol
scaleFactor = pow(new_rho/currentDensity, -1./3)
sim.ScaleSystem(scaleFactor)
      
# create integrator object
itg = rumd.IntegratorNVT(targetTemperature=T, timeStep=0.005)
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

nStepsPrBlock = 2**17
nBlocks = 100
nSteps = nBlocks*nStepsPrBlock 
sim.SetBlockSize(nStepsPrBlock)

sim.Run(nSteps)
	    
sim.WriteConf("end.xyz.gz")

# put all post processing below

sim.sample.TerminateOutputManagers()

# statistics
rs = rumd.Tools.rumd_stats()
rs.ComputeStats()
meanVals = rs.GetMeanVals()
meanSqVals = rs.GetMeanSqVals()
pressure = meanVals["p"] # the keys are the symbols in the file meta-data
pe = meanVals["pe"]
pe_var = meanSqVals["pe"] - pe**2
# to write the file that the command-line rumd_stats program writes:
rs.WriteStats()
# to print the stats summary to standard output:
rs.PrintStats()

# RDF
rdf_obj = rumd.Tools.rumd_rdf()
# constructor arguments: number of bins and minimum time
rdf_obj.ComputeAll(1000, 100.0)
rdf_obj.WriteRDF("rdf.dat")
