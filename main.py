from qiskit import QuantumCircuit, transpile, QuantumRegister, AncillaRegister
from qiskit.quantum_info import Operator
from qiskit_aer import AerSimulator
import numpy as np

# Example unitary matrix
unitary_matrix = np.array([[0, 1], 
                           [1, 0]])

# Create a unitary gate
unitary_gate = Operator(unitary_matrix)

# Create a quantum register with 2 data qubits and 1 ancilla qubit
qr = QuantumRegister(2, 'q')
anc = AncillaRegister(1, 'anc')
qc = QuantumCircuit(qr, anc)

# Apply the unitary gate to qubits 0 and 1
qc.unitary(unitary_gate, [qr[0]], label='U')

# Use the ancilla qubit in another operation, e.g., a CNOT
qc.cx(qr[0], anc[0])

# Visualize the circuit
print(qc)

# Print ancillas in the circuit
print("Ancilla qubits:", qc.ancillas)

# work in progress