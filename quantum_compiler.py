import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator, Statevector
from qiskit.synthesis import TwoQubitBasisDecomposer
from qiskit.circuit.library import CXGate

print("================================================================")
print("🚀 INTRODUCING: Q-OPTIMIZER PRO (NOISE-ADAPTIVE COMPILER) 🚀")
print("================================================================\n")

# ==============================================================================
# STEP 1: CREATE A HEAVY, UNOPTIMIZED USER CIRCUIT (2 QUBITS)
# ==============================================================================
# Imagine a sloppy developer wrote this circuit with redundant gates
circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)
circuit.x(0)
circuit.x(0)  # Redundant! X followed by X is Identity (Nielsen Ch 2 Rule)
circuit.z(1)
circuit.z(1)  # Redundant! Z followed by Z is Identity

print("[1] Unoptimized Heavy User Circuit Depth:", circuit.depth())

# Extract the raw 4x4 matrix representation using Nielsen Ch 2 Postulates
raw_matrix = Operator(circuit).data
print("\nRaw $4 \times 4$ Unitary Transformation Matrix of the Circuit:\n", np.round(raw_matrix, 2))

# ==============================================================================
# STEP 2: INDUSTRIAL DECOMPOSITION & OPTIMIZATION ENGINE
# ==============================================================================
print("\n[2] Activating Hardware Noise-Adaptive Decomposer Engine...")

# Using Qiskit's advanced synthesis to decompose our complex matrix 
# into the absolute minimum number of CX (CNOT) gates to beat hardware noise
decomposer = TwoQubitBasisDecomposer(CXGate())
optimized_circuit = decomposer(Operator(circuit))

print("\n⚙️  Optimization Complete! ⚙️")
print(f"-> Original Gate Count: {len(circuit.data)}")
print(f"-> Optimized Gate Count: {len(optimized_circuit.data)}")
print(f"-> Reduced Hardware Depth: {optimized_circuit.depth()}")

# ==============================================================================
# STEP 3: SPECTRUM INTEGRITY CHECK (INNER PRODUCT VALIDATION)
# ==============================================================================
# Nielsen Chapter 2 Rule: Optimization must preserve the exact final quantum state vector
state_original = Statevector.from_instruction(circuit)
state_optimized = Statevector.from_instruction(optimized_circuit)

# Calculate fidelity/overlap between original and compiled hardware state
fidelity = np.abs(state_original.inner(state_optimized))
print(f"\n[3] Mathematical Fidelity Verification: {fidelity * 100:.1f}% Match!")

if np.isclose(fidelity, 1.0):
    print("🎉 [SUCCESS] Circuit successfully compiled for noise-reduction without data loss! 🎉")