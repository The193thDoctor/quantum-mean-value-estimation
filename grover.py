from qiskit import QuantumCircuit, QuantumRegister, AncillaRegister
from qiskit_aer import AerSimulator
from qiskit.circuit.library import GroverOperator

from oracle import BaseOracle

def construct_grover_circuit(oracle:BaseOracle, num_iterations):
    if oracle.oracle is None:
        ValueError('Oracle is not set')
    num_qubits = oracle.num_qubits
    num_ancillas = oracle.num_ancillas

    qr = QuantumRegister(num_qubits, 'q')
    anc = AncillaRegister(num_ancillas, 'anc')
    qc = QuantumCircuit(qr, anc)
    qc.save_statevector(label='init') # for sanity check in case

    # Apply Hadamard gates to all qubits
    qc.h(qr[:] + anc[:])

    # Grover circuit
    for t in range(num_iterations):
        qc.save_statevector(label=f't={t}')
        grover_op = GroverOperator(oracle.oracle, insert_barriers=True)
        qc.append(grover_op, qr[:] + anc[:])

    qc.save_statevector(label=f't={num_iterations}')
    print(qc.decompose(reps=2).draw())

    return qc

