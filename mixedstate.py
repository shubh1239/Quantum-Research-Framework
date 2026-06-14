import numpy as np 
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)
# Apply a Hadamard gate to create a superposition state
qc.h(0)
# Simulate the circuit to get the state vector
simulator = AerSimulator()
qc.save_statevector()
result = simulator.run(qc).result()
state_vector = result.get_statevector()
print("State Vector after Hadamard gate:\n", state_vector)
# Now let's create a mixed state by applying a depolarizing channel
from qiskit_aer.noise import depolarizing_error
# Define a depolarizing error with a certain probability
error = depolarizing_error(0.1, 1)  # 10% depolarizing error
# Apply the error to the state vector
# Corrected: Converted to DensityMatrix first, because a Statevector cannot evolve under non-unitary noise channels directly
from qiskit.quantum_info import DensityMatrix
mixed_state = DensityMatrix(state_vector).evolve(error)
print("\nMixed State after applying depolarizing error:\n", mixed_state)

# Now let's simulate the measurement of the mixed state
qc_measure = QuantumCircuit(1, 1)
qc_measure.h(0)
qc_measure.measure(0, 0)
# Simulate the circuit to get the measurement results
result = simulator.run(qc_measure).result()
counts = result.get_counts()
print("\nMeasurement Counts for the Mixed State:\n", counts)

#Now calculate the density matrix for the mixed state
from qiskit.quantum_info import DensityMatrix
density_matrix = DensityMatrix(mixed_state)
print("\nDensity Matrix of the Mixed State:\n", density_matrix.data)

#Now calculate the purity of the mixed state
purity = np.trace(density_matrix.data @ density_matrix.data)
print("\nPurity of the Mixed State:", purity)

#Now lets code the same using numpy to simulate the mixed state and its properties:
# Define the pure state |ψ⟩ = (|0⟩ + |1⟩) / √2
pure_state = np.array([[1/np.sqrt(2)], [1/np.sqrt(2)]])
print("Pure State |ψ⟩:\n", pure_state)
# Create a mixed state by taking a convex combination of the pure state and the maximally mixed state
maximally_mixed_state = np.eye(2) / 2  # Maximally mixed state for a single qubit
mixed_state = 0.7 * pure_state @ pure_state.T + 0.3* maximally_mixed_state
print("\nMixed State ρ:\n", mixed_state)
# Calculate the purity of the mixed state
purity = np.trace(mixed_state @ mixed_state)
print("\nPurity of the Mixed State:", purity)