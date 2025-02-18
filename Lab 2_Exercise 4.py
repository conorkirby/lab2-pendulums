# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 12:34:37 2023

@author: Conor Kirby
"""
'''Exercise 4: Dampening the Non-Linear Pendulum'''
import numpy as np
import matplotlib.pyplot as plt

g = 9.8 #m/s
L = 9.8 #m
k = 0.5
A = 0.0

phi = 2/3
theta = 3.0
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

for i in range(3000):
    
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

plt.plot(t_list, omega_list, '-b')
plt.title("Damped Non-Linear Pendulum (Omega vs Time)") 
plt.xlabel("Time (s)")
plt.ylabel("Omega (rads)")
plt.grid()
#plt.savefig('C:/Users/Conor Kirby/OneDrive/Desktop/Computational Lab/Lab 2/Lab 2 Figures/DampedNonLin__Theta.pdf')
plt.show()

plt.plot(t_list, theta_list, '-r')
plt.title("Damped Non-Linear Pendulum (Theta vs Time)")
plt.xlabel("Time (s)")
plt.ylabel("Theta (rads)")
plt.grid()
#plt.savefig('C:/Users/Conor Kirby/OneDrive/Desktop/Computational Lab/Lab 2/Lab 2 Figures/DampedNonLin__Omega.pdf')
plt.show()
