# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 01:50:16 2014

@author: dzedzar
"""

import numpy as np

class PopulationActivity:
    def __init__(self,topology):
        self.topology = topology        
        self.activity = np.zeros(topology)
        self.input = np.zeros(topology)
        self.spike = np.false(topology)
        return
        
    def cycle(self):
        #will get activity from input
        #will check if there are spikes        
        pass        
        
    def output(self):
        #will set the output         
        pass
        
    def save(self,fileName):
        #will have to save to file
        pass
    
    def load(self,fileName):
        #will have to load from file
        pass
    
class IaFPopulation (PopulationActivity):
    def __init__(self,topology,spkThreshold,restPotential,memTConst,memResit):
        self.topology = topology        
        self.activity = np.zeros(topology)
        self.input = np.zeros(topology)
        self.spike = np.array(np.zeros(topology),btype=bool)
        
        self.spkThreshold = spkThreshold
        self.memTConst = memTConst
        self.memResit = memResit
        self.restPotential = restPotential
    
    def cycle(self,dt=0.0005):
        self.activity[np.where(self.spike)] = self.restPotential
        self.activity += (dt/self.membraneTimeConstant)*(self.memResit*self.input+(self.restPotential-self.activity))
        self.spike = self.activity>self.spkThreshold
        self.activity[np.where(self.spike)] = 0
    
    def output(self):
        return self.spike
        
class EMAXPopulation (PopulationActivity):
    def __init__(self,topology,emax=0.9):
        self.topology = topology
        self.emax = emax
        
    def cycle(self,dt=0.0005):
        emax_val = np.max(self.input)
        self.activity = self.input-self.emax*emax_val
        self.activity[np.where(self.activity<0)] = 0
        
    def output(self):
        return self.activity
        
class IziPopulation (PopulationActivity):
    def __init__(self,topology=1,aaa=0.02,bbb=0.2,ccc=-65,ddd=8,spkThreshold=30):
        self.topology = topology
        self.input = np.zeros(topology)
        self.spike = np.array(np.zeros(topology),dtype=bool)
        self.spkThreshold = spkThreshold        
        
        self.a = aaa
        self.b = bbb
        self.c = ccc
        self.d = ddd
        self.v = ccc * np.ones(self.topology)
        self.u = bbb * self.v       
        
    def cycle(self,dt=0.5):
        self.v[self.spike] = self.c
        self.u[self.spike] += self.d        
        self.v+=dt*(0.04*self.v**2+5*self.v+140-self.u+self.input)
        self.u+=self.a*(self.b*self.v-self.u) 
        self.spike[:] = False
        self.spike[self.v > self.spkThreshold] = True
    
    def output(self):
        return self.spike
        
    def potential(self):
        return self.v
        
class HHPopulation (PopulationActivity):
    
    def __init__(self,topology):
        self.topology = topology
        self.input = np.zeros(topology)
        
        self.m = np.zeros(topology)
        self.n = np.zeros(topology)
        self.h = np.zeros(topology)
        
        self.Cm = 0.01
        self.ena = 55.17
        self.ek = -72.14
        self.el = -49.42
        self.gna = 1.2
        self.gk = 0.36
        self.gl = 0.003
        
        self.v = self.el*np.ones(topology)
  
    def cycle(self,dt=0.0005):
        self.v +=   (dt/self.Cm) * (
                    self.input - \
                    self.gna*self.m**3*self.h*(self.v-self.ena) - \
                    self.gk*self.n**4*(self.v-self.ek) - \
                    self.gl*(self.v-self.el))
        
        an = 0.01*(self.v+50)/(1-np.exp((50-self.v)/10))
        am = 0.1*(self.v+35)/(1-np.exp((35-self.v)/10))
        ah = 0.07*np.exp(-0.05*(self.v-60))
        bn = 0.125*np.exp((60-self.v)/80)
        bm = 40*np.exp(-0.00556*(self.v+60))
        bh = 1/(1+np.exp((30-self.v)/10))
                                                        
        self.n += dt*(an*(1-self.n)-bn*self.n)        
        self.m += dt*(am*(1-self.m)-bm*self.m)        
        self.h += dt*(ah*(1-self.h)-bh*self.h)        
    
    def output(self):
        return self.v
        
    def potential(self):
        return self.v
    
   