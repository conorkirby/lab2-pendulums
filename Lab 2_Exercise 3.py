# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 11:36:10 2023

@author: Conor Kirby
"""
''''Exercise 3: Using the Runge Kutta Integration System'''

import numpy as np
import matplotlib.pyplot as plt

g = 9.8 #m/s
L = 9.8 #m
k = 0.0
A = 0.0

phi = 2/3
theta = 3.1415
omega = 0.0

t = 0.0
dt = 0.01

def f(theta, omega, t): #-k*omega is the dampening term
    return (-g/L)*np.sin(theta) - k*omega + A*np.cos(phi*t)
#print(f(1,2,3))

'''Runge-Kutta Algorithm'''

nsteps_list = []
nsteps = 0
theta_list = []
omega_list = []
t_list = []

for i in range(2000):
    
    k1a = dt * omega
    k1b = dt * f(theta, omega, t)
    
    k2a = dt * (omega + k1b/2)
    k2b = dt * f(theta + k1a/2, omega + k1b/2, t + dt/2)
    
    k3a = dt * (omega + k2b/2)
    k3b = dt * f(theta + k2a/2, omega + k2b/2, t + dt/2)
    
    k4a = dt * (omega + k3b)
    k4b = dt * f(theta + k3a, omega + k3b, t + dt)
    
    theta = theta + (k1a + 2*k2a + 2*k3a + k4a) / 6
    omega = omega + (k1b + 2*k2b + 2*k3b + k4b) / 6
    
    t = t + dt
    t_list.append(t)
    
    theta_list.append(theta)
    omega_list.append(omega)
    
    nsteps += 1
    nsteps_list.append(nsteps)

plt.plot(t_list, theta_list, '-r')
plt.title("Runge-Kutta Alogrithm vs Trapezoidal Rule")

plt.xlabel("Time (s)")
plt.ylabel("Theta (rads)")
plt.grid()


'''Trapeziodal Rule Algorithm'''
phi = 2/3
theta = 3.1415
omega = 0.0

t = 0.0
dt = 0.01

nsteps_list = []
nsteps = 0
theta_list = []
omega_list = []
t_list = []

for i in range(2000):
    
    k1a = dt * omega
    k1b = dt * f(theta, omega, t)
    k2a = dt * (omega + k1b)
    k2b = dt * f(theta + k1a, omega + k1b, t + dt)
    
    theta = theta + (k1a + k2a) / 2
    omega = omega + (k1b + k2b ) / 2
    
    t = t + dt
    
    t_list.append(t)
    
    theta_list.append(theta)
    omega_list.append(omega)
    
    nsteps += 1
    nsteps_list.append(nsteps)

plt.plot(t_list, theta_list, '--b')
plt.legend(["Runge-Kutta", "Trapeziodal Rule"])
plt.savefig('C:/Users/Conor Kirby/OneDrive/Desktop/Computational Lab/Lab 2/Lab 2 Figures/RK vs TrapRule time.pdf')
plt.show()

'''The algorithms plot identically proving that the new Runge-Kutta method works the same as the trapezoidal'''