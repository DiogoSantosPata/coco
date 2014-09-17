# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 01:58:35 2014

@author: dzedzar
"""

import numpy as np

class Synapse:
      def __init__(self,outputSize,outputUse,inputSize):
          self.outputSize = outputSize
          self.inputUse = inputUse
          self.inputSize = inputSize
          self.connectionMatrix = []
          self.weights = []
          
      def initWeights(self,distType='normal',mean=0,stdev=0):
          if initType == 'normal':
              self.weights = np.random.normal((self.outputSize,self.inputUse))
          else if initType == 'uniform':
              self.weights = np.zeros((self.outputSize,self.inputUse))
          else if initType == 'randomreal'
    
    