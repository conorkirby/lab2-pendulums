# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 12:52:50 2023

@author: Conor Kirby
"""

'''Exercise 5: The damped, driven non-linear pendulum'''

import numpy as np
import matplotlib.pyplot as plt

g = 9.8 #m/s
L = 9.8 #m
k = 0.5
A = 1.47

phi = 2/3
theta = 3
omega = 0.0

t = 0.0
dt = 0.01

def f(theta, omega, t): #-k*omega is the dampening term
    return (-1)*np.sin(theta) - k*omega + A*np.cos(phi*t)
#print(f(1,2,3))

'''Runge-Kutta Algorithm'''

iteration_number = 0
theta_list = []
omega_list = []
t_list = []
q= 180

transient = 18000

for i in range(30000):
    
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
    
    if (np.abs(theta) > np.pi + q):
        theta -= 2 * (np.pi)* np.abs(theta) / theta
    
    if iteration_number >= transient:
        
        theta_list.append(theta)
        omega_list.append(omega)
        t_list.append(t)
        
    iteration_number += 1

#print(theta_list, omega_list, newt)



plt.plot(theta_list, omega_list, '-m')
plt.title("Phase Portrait")
plt.xlabel("Theta [rads]")
plt.ylabel("Omega [rads]")
plt.grid()
plt.savefig('C:/Users/Conor Kirby/OneDrive/Desktop/Computational Lab/Lab 2/Lab 2 Figures/phaseportrait1.47.pdf')
plt.show()



