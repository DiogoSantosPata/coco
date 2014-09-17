# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 10:44:32 2014

@author: dzedzar
"""

import numpy as np

class ActivityTraceList:
     def __init__(self):
         self.list = []
         self.values = []
         
     def add(self,attribute):
         self.list.append(attribute)
         self.values.append([])
         
     def cycle(self):
         for ii in range(len(self.list)):
             self.values[ii].append(self.list[ii].activity)
             
    def saveToFile(self,filename):
        pass
    
    def loadFromFile(self,filename):
        pass

             
         
    
         