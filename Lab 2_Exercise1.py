# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:05:40 2023

@author: Conor Kirby
"""

import numpy as np
import matplotlib.pyplot as plt

g = 9.8 #m/s
L = 9.8 #m
k = 0.0
A = 0.0

phi = 2/3
theta = 1.0
omega = 0.0

t = 0.0
dt = 0.01
nsteps = 0

def f(theta, omega, t):
    return (-g/L)*theta - k*omega + A*np.cos(phi*t)

print(f(1,2,3))

nsteps_list = []
nsteps = 0
theta_list = []
omega_list = []
t_list = []

for i in range(1000):
    
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
'''    
plt.plot(nsteps_list, omega_list, '-m')
plt.plot(nsteps_list, theta_list, '-r')
plt.title("Simple Pendulum Oscillations")
plt.legend(["Omega", "Theta"])
plt.xlabel("Number of Steps")
plt.ylabel("Angle (rads)")
plt.axis([0, 500, -1.5, 1.5])
plt.grid()
#plt.savefig('C:/Users/Conor Kirby/OneDrive/Desktop/0.0,1.0.pdf')
plt.show()
'''
plt.plot(t_list, omega_list, '-m')
plt.plot(t_list, theta_list, '-r')
plt.title("Simple Pendulum Oscillations")
plt.legend(["Omega", "Theta"])
plt.xlabel("Time (s)")
plt.ylabel("Angle (rads)")
plt.axis([0, 5, -1.5, 1.5])
plt.grid()
plt.savefig('C:/Users/Conor Kirby/OneDrive/Desktop/Computational Lab/Lab 2/Lab 2 Figures/lin1.0,0.0time.pdf')
plt.show()