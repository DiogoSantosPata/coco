# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 19:32:05 2014

@author: dzedzar
"""

#import numpy as np

# WILL CREATE A TRAJECTORY AND PLOT IT

import cocoTrajectory as ctt

reload(ctt)

traj1 = ctt.Trajectory()
traj1.build()
#traj1.plot()

# WILL CREATE AN OCCUPATION MAP

import cocoRateMap as crm

reload(crm)

ratemap1 = crm.RateMap((1,20,20),[0,100,0,100])
ratemap1.buildOccMap(traj1)
ratemap1.plotOccMap()


# WILL CREATE SOME NEURONS AND PLOT THEM

#import cocoNeuronPopulation as cn
#import cocoTrace as ct
#
#reload(cn)
#reload(ct)
#
#Izi = cn.IziPopulation(10)
#HH = cn.HHPopulation(10)
#traceIzi = ct.Trace(Izi.potential)
#traceHH = ct.Trace(HH.potential)
#
#Izi.input[:] = np.random.uniform(0,10,10)
#HH.input[:] = Izi.input[:] 
#
#traceIzi.cycle()
#traceHH.cycle()
#
#for ii in range(1000):
#    Izi.cycle()
#    HH.cycle()
#    traceIzi.cycle()
#    traceHH.cycle()
#    
    