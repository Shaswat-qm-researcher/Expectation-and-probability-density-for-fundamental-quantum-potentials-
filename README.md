# Expectation Values and Probability Distributions for Quantum Eigenfunctions

## Overview


This code provides a fundamental numerical method for understanding quantum mechanical expectation values.  
By adjusting parameters such as $n$ or the type of potential, users can explore different quantum states and observe their behavior under various conditions. The Python 7 code calculates **expectation values of position and momentum** for quantum eigenfunctions.  
The code supports three quantum systems:

1. Particle in a Box  
2. Quantum Harmonic Oscillator  
3. Symmetric Double-Well Potential  

The script numerically evaluates and visualizes:
- Probability densities  
- Position expectation values  
- Momentum expectation values  

---

## Required Libraries

To run the code, the following Python libraries are required:

- `numpy` for numerical computations  
- `matplotlib` for plotting graphs  
- `scipy.special` for Hermite polynomials (used in harmonic oscillator and double-well eigenfunctions)  

Install them using:

```bash
pip install numpy==1.24.3 matplotlib==3.7.2 scipy==1.15.2
```

---

## Equations Used

### 1. Eigenfunctions for Different Quantum Systems

#### (a) Particle in a Box

Consider an infinite potential well. The normalized eigenfunction for a well of width $L$ is:

$$
\psi_n(x) = \sqrt{\frac{2}{L}} \sin\left( \frac{n\pi x}{L} \right)
$$

Where:  
- $n$ is the quantum number ($n = 1$ is the ground state, $n > 1$ for excited states)  
- $x$ is the position coordinate  

For this implementation, we assume $L = \pi$:

$$
\psi_n(x) = \sqrt{\frac{2}{\pi}} \sin(n x)
$$

#### (b) Harmonic Oscillator

Describes a particle under a quadratic potential:

$$
V(x) = \frac{1}{2} m \omega^2 x^2
$$

The normalized eigenfunctions are expressed using Hermite polynomials $H_n(x)$:

$$
\psi_n(x) = \frac{1}{\sqrt{2^n n! \sqrt{\pi}}} H_n(x) e^{-x^2 / 2}
$$

- These wavefunctions are Gaussian envelopes modulated by $H_n(x)$  
- The number of oscillations increases with $n$  

#### (c) Symmetric Double-Well Potential (Approximate)

The potential is:

$$
V(x) = x^4 - \alpha x^2
$$

Approximate eigenfunctions are:

$$
\psi_n(x) \approx e^{-x^4} H_n(x)
$$

This approximation captures:
- Wavefunction localization near potential wells  
- Tunneling behavior between wells  

---

### 2. Expectation Values

#### (a) Position Expectation Value

The expectation value of position:

$$
\langle x \rangle = \int x |\psi_n(x)|^2 \, dx
$$

#### (b) Momentum Expectation Value

Momentum is computed via the Fourier transform of $\psi(x)$:

$$
\langle p \rangle = \int k |\psi(k)|^2 \, dk
$$

Where:
- $\psi(k)$ is the momentum-space wavefunction

---

## How to Use the Code

1. Run the Python script.  
2. When prompted, input:
   - The desired quantum number $n$ (for ground or exited state) 
   - The potential type:  
     - `'particle_in_box'`  
     - `'harmonic_oscillator'`  
     - `'double_well'`  
3. The script will:
   - Compute $\langle x \rangle$ and $\langle p \rangle$  
   - Display plots for:
     - $|\psi(x)|^2$ — Probability density  
     - $|\psi(k)|^2$ — Momentum distribution  

---

## Output and Visualization

The script generates:

- **Probability Density Plot**:  
  Displays $|\psi(x)|^2$, the likelihood of finding a particle at different positions.

- **Momentum Distribution Plot**:  
  Shows $|\psi(k)|^2$, the probability distribution of momentum values.

These visualizations help analyze how a quantum state behaves in different potentials.
