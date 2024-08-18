from qiskit import QuantumCircuit, transpile, QuantumRegister, AncillaRegister
from qiskit_aer import AerSimulator
import numpy as np
import json

from oracle import BaseOracle, RyanOracle, SearchOracle
from grover import construct_grover_circuit
from plot import plot1d

json_path = 'test_case/2.json'
num_iterations = 5


def generate_oracle(oracle_class, json_path):
    with open(json_path, 'r') as f:
        samples = json.load(f)['samples']
    num_qubits = int(np.ceil(np.log2(len(samples))))
    if 2**num_qubits < len(samples):
        print('Number of samples is not a power of 2, zero-padding the samples')
        samples = np.pad(samples, (0, 2**num_qubits - len(samples)))
    oracle = oracle_class(num_qubits)
    oracle.set_oracle(samples)
    return oracle


oracle = generate_oracle(oracle_class=SearchOracle, json_path=json_path)
qc = construct_grover_circuit(oracle, num_iterations)

simulator = AerSimulator()
qc = transpile(qc, simulator)

result = simulator.run(qc).result()
state_vectors = []
for t in range(num_iterations+1):
    state_vectors.append(result.data()[f't={t}'])

plot1d(state_vectors)


