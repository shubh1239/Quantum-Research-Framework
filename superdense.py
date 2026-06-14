import numpy as np 
#superdense coding is a quantum communication protocol that allows two parties, Alice and Bob, to communicate two classical bits of information using only one qubit. The protocol relies on the use of entanglement, which is a unique property of quantum systems.
#lets see how superdense coding works step by step:
#1. Alice and Bob share an entangled pair of qubits, which we can represent as the Bell state |Φ+⟩ = (|00⟩ + |11⟩) / √2. This means that Alice has one qubit and Bob has the other qubit, and they are in a superposition of both being 0 and both being 1.
#2. Alice wants to send two classical bits of information (let's say 00, 01, 10, or 11) to Bob. To do this, she applies one of four possible operations to her qubit based on the two bits she wants to send:
#   - If she wants to send 00, she does nothing (identity operation).
#   - If she wants to send 01, she applies the Pauli-X gate (which flips the qubit).
#   - If she wants to send 10, she applies the Pauli-Z gate (which adds a phase of -1 to the |1⟩ state).
#   - If she wants to send 11, she applies the Pauli-Y gate (which combines the effects of X and Z).
#3. After applying the appropriate operation, Alice sends her qubit to Bob.
#4. Bob now has both qubits (the one he originally had and the one Alice sent). He performs a joint measurement on the two qubits in the Bell basis, which allows him to determine which of the four operations Alice applied.
#5. Based on the measurement outcome, Bob can decode the two classical bits that Alice sent. For example:
#   - If he measures |Φ+⟩, he knows Alice sent 00.
#   - If he measures |Φ-⟩, he knows Alice sent 01.
#   - If he measures |Ψ+⟩, he knows Alice sent 10
#   - If he measures |Ψ-⟩, he knows Alice sent 11.

#lets code the superdense using numpy to simulate the quantum states and operations:
zero = np.array([[1], [0]])  # |0⟩
one = np.array([[0], [1]])   # |1⟩
bit0 = np.kron(zero, zero)  # |00⟩
bit1 = np.kron(zero, one)   # |01⟩
bit2 = np.kron(one, zero)   # |10⟩
bit3 = np.kron(one, one)    # |11⟩
# Create the Bell state |Φ+⟩
bell_state = (bit0 + bit3) / np.sqrt(2)
# Define the operations for Alice
def apply_operation(state, operation):
    if operation == '00':
        return state  # Identity
    elif operation == '01':
        return np.kron(np.array([[1, 0], [0, -1]]), np.eye(2)) @ state  # Z gate
    elif operation == '10':
        return np.kron(np.array([[0, 1], [1, 0]]), np.eye(2)) @ state  # X gate
    elif operation == '11':
        return np.kron(np.array([[0, -1j], [1j, 0]]), np.eye(2)) @ state  # Y gate
    else:
        raise ValueError("Invalid operation")
# Simulate Alice sending the bits '10' to Bob
alice_operation = '10'
alice_state = apply_operation(bell_state, alice_operation)
# Simulate Bob's measurement in the Bell basis
def measure_bell_basis(state):
    bell_basis = [
        (bit0 + bit3) / np.sqrt(2),  # |Φ+⟩
        (bit0 - bit3) / np.sqrt(2),  # |Φ-⟩
        (bit1 + bit2) / np.sqrt(2),  # |Ψ+⟩
        (bit1 - bit2) / np.sqrt(2)   # |Ψ-⟩
    ]
    probabilities = [np.abs(np.dot(basis.T, state))**2 for basis in bell_basis]
    return np.argmax(probabilities)
# Bob measures the state
measurement_result = measure_bell_basis(alice_state)
# Decode the measurement result to get the original bits
if measurement_result == 0:
    decoded_bits = '00'
elif measurement_result == 1:
    decoded_bits = '01'
elif measurement_result == 2:
    decoded_bits = '10'
elif measurement_result == 3:
    decoded_bits = '11'
print(f"Alice sent: {alice_operation}")
print(f"Bob decoded: {decoded_bits}")

#now lets code using qiskit to implement superdense coding:
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
# Create a quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)
# Step 1: Create the Bell state |Φ+⟩
qc.h(0)  # Apply Hadamard gate to the first qubit
qc.cx(0, 1)  # Apply CNOT gate to entangle the qubits
# Step 2: Alice applies the operation based on the bits she wants to send
def apply_alice_operation(qc, bits):
    if bits == '00':
        pass  # Identity
    elif bits == '01':
        qc.z(0)  # Z gate
    elif bits == '10':
        qc.x(0)  # X gate
    elif bits == '11':
        qc.y(0)  # Y gate
    else:
        raise ValueError("Invalid bits")
# Alice wants to send '10'
alice_bits = '10'
apply_alice_operation(qc, alice_bits)
# Step 3: Alice sends her qubit to Bob (in this simulation, we just proceed to measurement)
# Step 4: Bob performs a joint measurement in the Bell basis
qc.cx(0, 1)  # Apply CNOT gate
qc.h(0)  # Apply Hadamard gate
qc.measure([0, 1], [0, 1])  # Measure both qubits
# Execute the circuit on a simulator
simulator = AerSimulator()
result = simulator.run(qc, shots=1).result()
counts = result.get_counts(qc)
# Decode the measurement result to get the original bits
measured_bits = list(counts.keys())[0]
print(f"Alice sent: {alice_bits}")
print(f"Bob measured: {measured_bits}")

