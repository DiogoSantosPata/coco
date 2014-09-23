# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 20:13:40 2014

@author: dzedzar
"""

import numpy as np

# will return the occupation map
def cocoOccMap(positions,mapRange,topology,dt,sigma2=10):
    xxx = np.linspace(mapRange[0],mapRange[1],topology[0])        
    yyy = np.linspace(mapRange[2],mapRange[3],topology[1])
    xxx,yyy = np.meshgrid(xxx,yyy)
    ttt = np.ravel(xxx)+1j*np.ravel(yyy)
    occ = np.zeros(ttt.shape)    
    for ii in range(len(ttt)):
        occ[ii] = np.sum(np.exp(-1*abs(ttt[ii]-positions)/sigma2))*dt
    occ = occ.reshape(topology)
    return occ
    
def cocoRateMapSpike(spikePositions,occMap,mapRange,topology,sigma2=10):
    xxx = np.linspace(mapRange[0],mapRange[1],topology[0])        
    yyy = np.linspace(mapRange[2],mapRange[3],topology[1])
    xxx,yyy = np.meshgrid(xxx,yyy)
    ttt = np.ravel(xxx)+1j*np.ravel(yyy)
    rateMap = np.zeros(ttt.shape)    
    for ii in range(len(ttt)):
        rateMap[ii] = np.sum(np.exp(-1*abs(ttt[ii]-spikePositions)/sigma2))
    rateMap = rateMap.reshape(topology)
    rateMap /= occMap
    return rateMap

def cocoRateMapRate(positions,rates,mapRange,topology,sigma2=10):
    xxx = np.linspace(mapRange[0],mapRange[1],topology[0])        
    yyy = np.linspace(mapRange[2],mapRange[3],topology[1])
    xxx,yyy = np.meshgrid(xxx,yyy)
    ttt = np.ravel(xxx)+1j*np.ravel(yyy)
    rateMap = np.zeros(ttt.shape)    
    for ii in range(len(ttt)):     
        rateMap[ii] = np.sum(rates*np.exp(-1*abs(ttt[ii]-positions)/sigma2))/np.sum(np.exp(-1*abs(ttt[ii]-positions)/sigma2))
    rateMap = rateMap.reshape(topology)
    return rateMap
        
            
        