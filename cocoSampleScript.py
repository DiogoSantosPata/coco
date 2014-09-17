# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 19:32:05 2014

@author: dzedzar
"""

import numpy as np

# WILL CREATE A TRAJECTORY AND PLOT IT

import cocoTrajectory as ctt

reload(ctt)

ttt = ctt.Trajectory()
ttt.build()
ttt.plot()


# WILL CREATE SOME NEURONS AND PLOT THEM

import cocoNeuronPopulation as cn
import cocoTrace as ct

reload(cn)
reload(ct)

aaa = cn.IziPopulation(10)
bbb = cn.HHPopulation(10)
ttt = ct.Trace(aaa.potential)
ttt2 = ct.Trace(bbb.potential)

aaa.input[:] = np.random.uniform(0,10,10)
bbb.input[:] = aaa.input[:] 

ttt.cycle()
ttt2.cycle()

for ii in range(1000):
    aaa.cycle()
    bbb.cycle()
    ttt.cycle()
    ttt2.cycle()
    
    