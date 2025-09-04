from qiskit import QuantumCircuit, transpile
from qiskit.visualization import circuit_drawer
from qiskit_ibm_runtime.fake_provider import FakeManilaV2
from qiskit_aer.noise import NoiseModel
from qiskit_aer import AerSimulator
import random
from scipy.stats import multivariate_normal
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from .resource_path import quantum_circuit_image
from .resource_path import *

def createCircuit():
    qc = QuantumCircuit(3)
    qc.h([0, 1, 2])
    qc.measure_all()

    filename = quantum_circuit_image()
    # Reduce figsize for a smaller image (width, height in inches)
    circuit_drawer(qc, output='mpl', filename=filename)

    return qc

def noisy_simulator(qc):
    # Use fake noisy backend
    fake_backend = FakeManilaV2()
    noise_model = NoiseModel.from_backend(fake_backend)
    simulator = AerSimulator(noise_model=noise_model)

    # Transpile circuit
    qc_t = transpile(qc, simulator)
    # Run simulation
    shots = 1024
    # Note: shots is set to 1024, but can be adjusted as needed.
    job = simulator.run(qc_t, shots=shots)
    result = job.result()
    counts = result.get_counts()
    return counts, shots

def returnSelectedState(counts):
    bitstrings = list(counts.keys())
    weights = list(counts.values())
    selected = random.choices(bitstrings, weights=weights, k=1)[0]
    return selected

def createAnimation(measured_state):
    states = ['000', '001', '010', '011', '100', '101', '110', '111']
    probabilities = [1/8] * 8

    state_map = {
        '000': (0, 0), '001': (0, 1), '011': (0, 2), '010': (0, 3),
        '100': (1, 0), '101': (1, 1), '111': (1, 2), '110': (1, 3)
    }

    x = np.linspace(-1, 4, 100)
    y = np.linspace(-1, 2, 100)
    X, Y = np.meshgrid(x, y)
    Z_frames = []
    sigma = 0.075
    frames = 30

    for frame in range(frames):
        t = frame / (frames - 1)
        Z_frame = np.zeros_like(X)

        for state, prob in zip(states, probabilities):
            row, col = state_map[state]
            mu = [col, row]
            rv = multivariate_normal(mean=mu, cov=[[sigma, 0], [0, sigma]])
            pdf_values = rv.pdf(np.dstack((X, Y)))
            bump = prob * pdf_values / pdf_values.max() * 0.9  # normalize and scale

            if state == measured_state:
                # Gradually increase dominance of measured state
                collapse_bump = bump / bump.max() * 1.0
                Z_frame += (1 - t) * bump + t * collapse_bump
            else:
                Z_frame += (1 - t) * bump

        Z_frames.append(Z_frame)

    fig = plt.figure(figsize=(12, 7))  # Larger canvas
    ax = fig.add_subplot(111, projection='3d')

    def animate(i):
        ax.clear()
        surf = ax.plot_surface(X, Y, Z_frames[i], cmap='plasma', edgecolor='none', antialiased=True)
        ax.set_xticks(np.arange(4))
        ax.set_xticklabels(['00', '01', '11', '10'])
        ax.set_yticks(np.arange(2))
        ax.set_yticklabels(['0', '1'])
        ax.set_xlabel("q1q2 (Gray code)", fontsize=12)
        ax.set_ylabel("q0", fontsize=12)
        ax.set_zlabel("|?|²", fontsize=12)
        ax.set_zlim(0, 1)
        ax.set_title(f"Wavefunction Collapse to |{measured_state}? ({int(measured_state, 2)}) (Frame {i+1}/{frames})", fontsize=14)
        return [surf]

    ani = animation.FuncAnimation(fig, animate, frames=frames, interval=100, blit=False)

    plt.close()
    ani.save(wf_collapse_gif_path(), writer='ffmpeg', fps=10, dpi=150)
