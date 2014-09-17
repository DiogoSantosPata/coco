# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 10:40:00 2014

@author: dzedzar
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage
import pickle
from scipy.interpolate import griddata

class RateMap:
    def __init__(self,topology,mapRange=[0,1,0,1]):
        self.mapRange = mapRange        
        self.topology = topology
        self.values = np.zeros(topology)
        
    def buildOccMap(self,trajectory):
        pass
    
    def buildRateMap(self,trajectory,activityTrace):
        pass

    def save(self,fileName):
        mapRange = self.mapRange        
        topology = self.topology
        values = self.values     
        with open(fileName, 'w') as ff:
            pickle.dump([mapRange, topology, values], ff)
    
    def load(self,fileName):
        with open(fileName, 'r') as ff:
            self.mapRange, self.topology, self.values = pickle.load(ff)

    def plot(self,cellNumber):
        plt.ion()
        plt.pcolormesh(self.values[cellNumber,:,:])
        plt.show()

    def interpolate(self,position,cells=[]):
 
        if not cells:
            cells = range(self.topology[0])
        if type(cells) is int:
            cells = [cells]
        xll = np.linspace(self.mapRange[0],self.mapRange[1],self.topology[1])        
        yll = np.linspace(self.mapRange[2],self.mapRange[3],self.topology[2])
        xll,yll = np.meshgrid(xll,yll)
        xll = np.ravel(xll)
        yll = np.ravel(yll)
        
        activity = np.zeros(len(cells))
        for ii in range(len(cells)):
            activity[ii] = griddata((xll, yll), np.ravel(self.values[cells[ii],:,:]), (np.real(position),np.imag(position)), method='cubic')        
        
        return activity

    
    ## LEC    
    
    def buildAbstractLEC(self,numberOfCells,spatialInfo):
        tempcells = np.zeros((numberOfCells,self.topology[1],self.topology[2]))
        for ii in range(numberOfCells):
            tempcells[ii,:,:] = self.__newLECCell(spatialInfo)
        ppp = np.random.randint(0,numberOfCells-1,self.topology[0])
        self.values = tempcells[ppp,:,:]          
    
    
    def __newLECCell(self,spatialInfo):
        
        lenX = self.topology[1]
        lenY = self.topology[2] 

        aa = np.random.uniform(0.,3., (5,5))
        for ind,val in np.ndenumerate(aa):	
		
            if aa[ind] > spatialInfo: aa[ind] = np.random.uniform(0.5,1)   # factorSensivel vai de 0 a 3
            else: aa[ind] = np.random.uniform(0,0.5)
		
            wanted_size = 100
            bb = np.zeros((wanted_size, wanted_size))
            for ii in range(wanted_size):
                for jj in range(wanted_size):
                    idx1 = ii * len(aa) / wanted_size
                    idx2 = jj * len(aa) / wanted_size
                    bb[ii][jj] = aa[idx1][idx2]
            bb = np.roll(bb,np.random.randint(0, min([lenX,lenY])  ),np.random.randint(0,2)   )
            celula = scipy.ndimage.filters.gaussian_filter(bb, 4)
	
        return celula    
    