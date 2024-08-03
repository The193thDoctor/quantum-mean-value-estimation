from qiskit import QuantumCircuit, transpile, QuantumRegister, AncillaRegister
from qiskit.quantum_info import Operator
from qiskit_aer import AerSimulator
import numpy as np

from oracle import Oracle

def ConstructGroverCircuit(oracle):
    num_qubits = oracle.num_qubits
    num_ancillas = oracle.num_ancillas

    qr = QuantumRegister(num_qubits, 'q')
    anc = AncillaRegister(num_ancillas, 'anc')
    qc = QuantumCircuit(qr, anc)

    # Apply Hadamard gates to all qubits
    qc.h(qr)
