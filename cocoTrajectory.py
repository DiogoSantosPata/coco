# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 10:39:29 2014

@author: dzedzar

"""
import numpy as np
import matplotlib.pyplot as plt
import pickle

class Trajectory:
    
    def __init__(self,fileName=[]):
        self.type = 'Trajectory'
        if type(fileName) is str:
            self.load(fileName)
        else:
            self.position = []
            self.angle = []
            self.time = []
            self.range = [0,100,0,100]
    
    def build(self,trajLenght=600,sampleRate=10,arenaRange=[0,100,0,100],noise=[1,0.1]):
    
        self.range = arenaRange
        rangee = trajLenght * sampleRate
        steep = 1/float(sampleRate)
        safeRange = 2        
        
        speedNoise = noise[0]
        angleNoise = noise[1]*np.pi
        
        self.time = np.array(range(rangee))*steep 
        self.angle = np.zeros(rangee)
        self.position = np.zeros(rangee) + 1j*np.zeros(rangee)        
        
        arenaX = [arenaRange[0],arenaRange[1]]
        arenaY = [arenaRange[2],arenaRange[3]]

        self.position[0] = arenaX[1]/2 + 1j*arenaY[1]/2
        self.angle[0] = np.random.uniform(-np.pi,np.pi) 
        
        for ii in range(1,rangee):

            self.angle[ii] = self.angle[ii-1]

            if(np.real(self.position[ii-1])<(arenaRange[0]+safeRange)):
                self.angle[ii]  = np.random.uniform(-0.48*np.pi,0.48*np.pi)
            
            if(np.real(self.position[ii-1])>(arenaRange[1]-safeRange)):
                self.angle[ii]  = np.random.uniform(0.52*np.pi,1.48*np.pi)
            
            if(np.imag(self.position[ii-1])<(arenaRange[2]+safeRange)):
                self.angle[ii]  = np.random.uniform(0.05*np.pi,0.95*np.pi)
            
            if(np.imag(self.position[ii-1])>(arenaRange[3]-safeRange)):
                self.angle[ii]  = np.random.uniform(1.05*np.pi,1.95*np.pi)
          
            self.position[ii] = self.position[ii-1] + 1*np.exp(1j*self.angle[ii])
            if(speedNoise > 0 and angleNoise>0):            
                self.position[ii] = self.position[ii] + np.random.normal(0,speedNoise)*np.exp(1j*np.random.normal(0,angleNoise))

    def interpolate(self,givenTimes):
        xxx = np.interp(givenTimes,self.time,np.real(self.position))        
        yyy = np.interp(givenTimes,self.time,np.imag(self.position))        
        angle = np.interp(givenTimes,self.time,self.angle)
        position = xxx + 1j*yyy
        return position, angle
    '''
    def plot(self):
        plt.clf()
        plt.plot(np.real(self.position),np.imag(self.position), '-')
        plt.xlim( min(np.real(self.position)) , max(np.real(self.position))   )
        plt.ylim( min(np.imag(self.position)) , max(np.imag(self.position))   )
        plt.title('Trajectory')
        plt.xlabel('X')
        plt.ylabel('Y')									
    '''

    def plot(self,axis=[]):        
        if(str(type(axis)) != "<class 'matplotlib.axes.AxesSubplot'>"):
            fg = plt.gcf()
            fg.clf()
            axis = plt.subplot(1,1,1)        
        axis.plot(np.real(self.position),np.imag(self.position),'k-')
        axis.set_xlim([self.range[0],self.range[1]])
        axis.set_ylim([self.range[2],self.range[3]])
        axis.xlabel('x')
        axis.ylabel('y')
        axis.title('Trajectory')
        fg.canvas.draw()
        plt.show()
        
        

    def save(self,fileName):
        position = self.position
        angle = self.angle
        time = self.time
        trange = self.range
        with open(fileName, 'w') as ff:
            pickle.dump([position, angle, time, trange], ff)
            
    def load(self,fileName):
        with open(fileName, 'r') as ff:
            self.position, self.angle, self.time, self.range = pickle.load(ff)

   