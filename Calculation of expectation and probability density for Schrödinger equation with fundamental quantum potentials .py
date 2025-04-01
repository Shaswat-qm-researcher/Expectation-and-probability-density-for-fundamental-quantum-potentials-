#!/usr/bin/env python
# coding: utf-8

# In[20]:


### import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hermite, factorial

def eigenfunction(n, x, potential_type="particle_in_box"):
    """Returns the normalized eigenfunction for a given quantum number n.
    Supports 'particle_in_box', 'harmonic_oscillator', and 'double_well'.
    """
    if potential_type == "particle_in_box":
        return np.sqrt(2 / np.pi) * np.sin(n * x)  # Infinite potential well
    elif potential_type == "harmonic_oscillator":
        normalization = 1.0 / np.sqrt(2**n * factorial(n) * np.sqrt(np.pi))
        return normalization * hermite(n)(x) * np.exp(-x**2 / 2)  # Harmonic oscillator eigenfunction
    elif potential_type == "double_well":
        return np.exp(-x**4) * hermite(n)(x)  # Approximate double well solution
    else:
        raise ValueError("Unsupported potential type")

def probability_expectation(n, potential_type="particle_in_box"):
    """Computes the expectation value of the probability distribution.
    Expectation value: \langle x \rangle = \int x |\psi_n(x)|^2 dx
    """
    x_range = (-5, 5) if potential_type in ["harmonic_oscillator", "double_well"] else (0, 2 * np.pi)
    x = np.linspace(*x_range, 500)
    psi = eigenfunction(n, x, potential_type)
    probability_density = psi ** 2
    expectation_x = np.trapz(x * probability_density, x)  # Numerical integration for position expectation
    
    # Compute momentum expectation using Fourier transform
    k = np.fft.fftfreq(len(x), d=(x[1] - x[0])) * (2 * np.pi)
    psi_k = np.fft.fft(psi)
    probability_momentum = np.abs(psi_k) ** 2
    expectation_p = np.trapz(k * probability_momentum, k)  # Numerical integration for momentum expectation
    
    return expectation_x, expectation_p, x, probability_density, k, probability_momentum

# User input and type conversion
n1 = int(input("Index of the first eigen function: "))
n2 = int(input("Index of the second eigen function: "))
potential_type = input("Enter potential type ('particle_in_box', 'harmonic_oscillator', 'double_well'): ")

# Compute expectation values and probability densities
exp_x1, exp_p1, x, prob_density1, k, prob_momentum1 = probability_expectation(n1, potential_type)
exp_x2, exp_p2, _, prob_density2, _, prob_momentum2 = probability_expectation(n2, potential_type)

# Print expectation values
print(f"Expectation value of position for n1 = {n1}: {exp_x1}")
print(f"Expectation value of momentum for n1 = {n1}: {exp_p1}")
print(f"Expectation value of position for n2 = {n2}: {exp_x2}")
print(f"Expectation value of momentum for n2 = {n2}: {exp_p2}")

# Plot probability densities
plt.figure(figsize=(8, 5))
plt.xlabel("x", fontsize=14, fontname='Arial')
plt.ylabel("$|\\psi|^2$", fontsize=14, fontname='Arial')
plt.xticks(fontsize=12, fontname='Arial')
plt.yticks(fontsize=12, fontname='Arial')
plt.tick_params(axis='both', direction='in', length=6, width=1.5)
plt.plot(x, prob_density1, label=f"n1 = {n1}", color="red", linewidth=1, linestyle = '--')
plt.plot(x, prob_density2, label=f"n2 = {n2}", color="black", linewidth=1)
plt.legend(fontsize=12, frameon=False)
plt.title(f"Probability Densities of Eigenfunctions ({potential_type})", fontsize=14, fontname='Arial')
plt.tight_layout()
plt.show()

# Plot momentum distributions
plt.figure(figsize=(8, 5))
plt.xlabel("Momentum k", fontsize=14, fontname='Arial')
plt.ylabel("$|\\psi(k)|^2$", fontsize=14, fontname='Arial')
plt.xticks(fontsize=12, fontname='Arial')
plt.yticks(fontsize=12, fontname='Arial')
plt.tick_params(axis='both', direction='in', length=6, width=1.5)
plt.plot(k, prob_momentum1, label=f"n1 = {n1}", color="royalblue", linewidth=1, linestyle = '--')
plt.plot(k, prob_momentum2, label=f"n2 = {n2}", color="orange", linewidth=1, linestyle = 'dotted')
plt.legend(fontsize=12, frameon=False)
plt.title(f"Momentum Distributions of Eigenfunctions ({potential_type})", fontsize=14, fontname='Arial')
plt.tight_layout()
plt.show()

