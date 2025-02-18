# Lab 2: The Pendulum

This repository contains the code and documentation for **Lab 2**, which explores the dynamics of **nonlinear pendulums** and the numerical methods used to solve their equations of motion. The lab focuses on understanding the behavior of pendulums under various conditions, including linear and nonlinear regimes, damping, and external driving forces. By solving coupled ordinary differential equations (ODEs) numerically, you will analyze the motion of pendulums and observe phenomena such as **chaos** and **period doubling**.

## Key Concepts
- **Nonlinear pendulum dynamics**: The equation of motion for a pendulum is nonlinear due to the \(\sin\theta\) term.
- **Linear approximation**: For small angles, \(\sin\theta \approx \theta\), simplifying the pendulum to a linear system.
- **Damping and driving forces**: Adding friction and external forces leads to complex behaviors like **limit cycles** and **chaotic motion**.
- **Numerical integration**: Using methods like the **trapezoid rule** and **Runge-Kutta** to solve ODEs.

## Lab Structure

The lab is divided into five exercises:

### 1. **Linear Pendulum**
- Solve the equation of motion for a **linear pendulum** (\(\sin\theta \approx \theta\)) using the trapezoid rule.
- Plot the angle (\(\theta\)) and angular velocity (\(\omega\)) as functions of time.
- Compare results for different initial conditions.

### 2. **Nonlinear Pendulum**
- Modify the code to solve the **nonlinear pendulum** equation (\(\sin\theta\) retained).
- Compare the motion of linear and nonlinear pendulums for the same initial conditions.
- Analyze how the nonlinear term affects the pendulum's behavior.

### 3. **Runge-Kutta Integration**
- Implement the **4th-order Runge-Kutta method** for more accurate numerical integration.
- Compare the results with the trapezoid rule for the nonlinear pendulum.

### 4. **Damped Nonlinear Pendulum**
- Introduce **damping** (friction) into the pendulum's motion.
- Analyze how damping affects the pendulum's amplitude and energy over time.

### 5. **Damped, Driven Nonlinear Pendulum**
- Add an **external driving force** to the damped pendulum.
- Study **periodic**, **aperiodic**, and **chaotic** motion using **phase portraits**.
- Explore phenomena like **limit cycles** and **period doubling**.

## Repository Contents
- **Python scripts** for each exercise, including numerical integration and plotting.
- **Documentation** explaining the physics and numerical methods used.
- **Plots** of angle, angular velocity, and phase portraits for various conditions.

## Usage
1. Clone the repository.
2. Run the Python scripts for each exercise to generate results and plots.
3. Modify parameters (e.g., damping coefficient, driving force amplitude) to explore different behaviors.

This lab provides a hands-on introduction to **nonlinear dynamics** and **chaos theory** using the pendulum as a model system. Feel free to explore and adapt the code for your own projects!
