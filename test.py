from qiskit.circuit import QuantumCircuit
from qiskit.circuit.library import GroverOperator
oracle = QuantumCircuit(2)
oracle.z(0)  # good state = first qubit is |1>
print(oracle.num_ancillas)
grover_op = GroverOperator(oracle, insert_barriers=True)
print(grover_op.decompose().draw())