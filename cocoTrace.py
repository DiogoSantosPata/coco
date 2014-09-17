# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 10:44:32 2014

@author: dzedzar
"""

import numpy as np
import matplotlib.pyplot as plt
import pickle

class Trace:
     def __init__(self,traceFunction=[]):
         self.values = []
         self.traceFunction = traceFunction         
         
     def setTraceFunction(self,traceFunction):
         self.traceFunction = traceFunction                 
         self.values = []         
         
     def cycle(self):
         self.values.append(np.copy(self.traceFunction()))
             
     def save(self,filename):
         with open(filename, 'w') as ff:
            pickle.dump([self.values], ff)
    
     def load(self,filename):        
         with open(filename, 'r') as ff:
            self.values = pickle.load(ff)        
            
     def output(self,whichData=1):
         if type(whichData) is int:
             whichData = [whichData]
         toOutput = np.zeros((len(self.values),len(whichData)))
         for ii in range(len(self.values)):
             toOutput[ii,:] = self.values[ii][whichData]
         return toOutput
             
     def plot(self,whichData=1):
         if type(whichData) is not list:
             whichData = [whichData]
         if len(whichData) is 0:
             whichData = range(len(self.values[0]))
         toOutput = np.zeros((len(self.values),len(whichData)))
         for ii in range(len(self.values)):
             toOutput[ii,:] = self.values[ii][whichData]
         plt.clf()
         #fig1 = plt.figure()
         plt.ion()
         for ii in range(len(whichData)):
             #plt.hold(True)
             plt.plot(range(len(self.values)), toOutput[:,ii], '-')         
         plt.show()
         
         