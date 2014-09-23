# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 10:44:32 2014

@author: dzedzar
"""

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import pickle

class Trace:       
                 
     def save(self,filename):
         with open(filename, 'w') as ff:
            pickle.dump([self.values], ff)
    
     def load(self,filename):        
         with open(filename, 'r') as ff:
            self.values = pickle.load(ff)        
    
class ActivityTrace (Trace):    
     def __init__(self,traceFunction=[]):
         self.type = 'ActivityTrace'
         self.traceFunction = traceFunction         
         self.values = np.array([])
         self.currentIndex = -1;
         self.time = []
         
     def setTraceFunction(self,traceFunction):
         self.traceFunction = traceFunction                 
         self.values = np.array([])  

     def prealloc(self,sizeOfMatrix):
         self.values = np.zeros(sizeOfMatrix)
    
     def realloc(self,sizeToAdd):
         aaa = self.values.shape
         self.values.resize((aaa[0],aaa[1]+sizeToAdd),refcheck=False)

     def cycle(self,dt=0.0005):
         self.currentIndex+=1
         if(self.values.shape[0] == 0):
             self.values = self.traceFunction()             
             self.time.append(0)
         else:    
             if((self.currentIndex+1)>self.values.shape[1]):
                 self.realloc(1)
             self.values[:,self.currentIndex] = self.traceFunction()
             self.time.append(self.time[-1]+dt)
            
     def output(self,whichData=1):
         if type(whichData) is int:
             whichData = [whichData]
         toOutput = self.values[whichData,:]
         #np.zeros((len(self.values),len(whichData)))
         #for ii in range(len(self.values)):
         #    toOutput[ii,:] = self.values[ii][whichData]
         return toOutput
             
     def plot(self,whichData=1):
         if type(whichData) is not list:
             whichData = [whichData]
         if len(whichData) is 0:
             whichData = range(len(self.values[0]))
         #toOutput = np.zeros((len(self.values),len(whichData)))
         #for ii in range(len(self.values)):
         #    toOutput[ii,:] = self.values[ii][whichData]
         toOutput = self.values[whichData,:]
         plt.clf()
         
         #########################################							
         plt.subplot(2,1,1)  # Top plot is a raster									
         for ith, cell in enumerate( whichData   ):
              plt.vlines(cell, ith + .5, ith + 1.5, color='k')
              plt.ylim(.5, len(whichData) + .5)
         plt.title('Raster plot')
         plt.ylabel('Cell')		
         
         plt.subplot(2,1,2)# Bottom hist
         plt.hist(whichData)#, np.arange(0, len(time)))
         plt.xlabel('Time')
         plt.show()
         #########################################	
						
         #fig1 = plt.figure()
         plt.ion()
         for ii in range(len(whichData)):
             #plt.hold(True)
             plt.plot(range(len(self.values)), toOutput[:,ii], '-')         
         plt.show()

     def fromRateMap(self,ratemap,trajectory,dt=[]):
         if isreal(dt):        
             ttt = arange(trajectory.time[0],trajectory.time[-1],dt)
         else:
             ttt = trajectory.time
         self.values = np.zeros((ratemap.topology[0],ttt.size))
         for ii in range(len(ttt)):
             self.values[:,ii] = ratemap.interpolate(trajectory.interpolate(ttt[ii]))             
             
         pass
         
         

class SpikeTrace (Trace):
     def __init__(self,traceFunction=[]):
         self.type = 'SpikeTrace'
         self.traceFunction = traceFunction         
         self.values = []
         self.currentIndex = -1
         self.numUnits = 0
         
     def setTraceFunction(self,traceFunction):
         self.traceFunction = traceFunction                 
         self.values = []  

     def cycle(self):
         self.values.append(np.where(self.traceFunction()>0))
         if len(self.values[-1]>0):         
             if (np.max(self.values[-1])+1)>self.numUnits:
                 self.numUnits = np.max(self.values[-1]) + 1
        
     def output(self,whichData=[]):
         if type(whichData) is not list:
             whichData = [whichData]
         if len(whichData) is 0:
             whichData = range(len(self.values[0]))
         outputData = []
         for ii in range(len(self.values)):
             for jj in self.values[ii]:
                 outputData[jj].append(ii)
         return outputData[whichData]                 
         
         # retunr a list of lists with the cells that spike each time        
        
     def matOutput(self,whichData=[]):
         if type(whichData) is not list:
             whichData = [whichData]
         if len(whichData) is 0:
             whichData = range(len(self.values[0]))
         outputMat = np.array(self.numUnits,len(self.values),dtype=bool)
         for ii in range(len(self.values)):
             outputMat[self.value[ii],ii] = True
         return outputMat[whichData,:]
         
     # get the times of spikes of each cell in a matrix
     
     def plot(self):
         pass
<<<<<<< HEAD
     # raster plot
=======
     # raster plot
>>>>>>> FETCH_HEAD
