import numpy as np 

#Computational Basis Kets as Column Vectors

ket_0 = np.array([[1.0 + 0.0j],
                  [0.0 + 0.0j]])
ket_1 = np.array([[0.0 + 0.0j],
                  [1.0 + 0.0j]])

# 2-Qubit Initial Computational State |00> using Kronecker Tensor Product
# Logic: |00> = |0> tensor |0>
state_2qubit = np.kron(ket_0, ket_0)

print("--- 2-Qubit Register Initialized ---")
print("Initial State |00> Vector:\n", state_2qubit)
print("-" * 40)

# Single Qubit Hardware Gates
I = np.array([[1.0 + 0.0j, 0.0 + 0.0j], 
              [0.0 + 0.0j, 1.0 + 0.0j]])

X = np.array([[0.0 + 0.0j, 1.0 + 0.0j], 
              [1.0 + 0.0j, 0.0 + 0.0j]])

# Task: We want to apply a gate on Qubit 1 and keep Qubit 2 unchanged.
# Composite Operator: Upper_Gate = X tensor I
X_on_qubit1 = np.kron(X, I)

print("\nComposite 4x4 Pauli-X Gate Matrix for Qubit 1:\n", X_on_qubit1)

print("\n=== Welcome to Quantum Core CLI Simulator ===")
print("Available Commands: 'X' (Flips Qubit 1), 'show' (Prints Current State), 'exit'")

while True:
    # Capturing user input directly via terminal
    user_choice = input("\nEnter quantum command: ").strip().lower()
    
    if user_choice == 'exit':
        print("Shutting down quantum register")
        break
        
    elif user_choice == 'x':
        # Nielsen Chapter 2 Matrix Multiplication: New_State = Gate * Current_State
        state_2qubit = np.dot(X_on_qubit1, state_2qubit)
        print("[SUCCESS] Pauli-X Gate applied to Qubit 1.")
        
    elif user_choice == 'show':
        print("\nCurrent 2-Qubit State Vector Components:")
        print(state_2qubit)
        
    else:
        print("[ERROR] Unknown command! Use 'X', 'show', or 'exit'.")