import abc
from qiskit import QuantumCircuit
from qiskit.circuit.library import UnitaryGate
import numpy as np


class Oracle(abc.ABC):
    def __init__(self, num_qubits):
        self.oracle = None
        self.num_qubits = num_qubits
        self.num_ancillas = None

    @abc.abstractmethod
    def set_oracle(self, values) -> QuantumCircuit:
        pass


class OracleRyan(Oracle):
    def __init__(self, num_qubits, input_dimension=1):
        super().__init__(num_qubits)
        self.num_ancillas = 0
        if input_dimension != 1:
            ValueError('Input dimension must be 1')

    def set_oracle(self, values):
        if len(values) != 1:
            ValueError('Input values must be of length 1')
        values = values[0]
        num_values = 2 ** self.num_qubits
        if len(values) > num_values:
            ValueError('Too many input values')
        values = np.pad(values, (0, num_values - len(values)), 'constant')
        unitary_matrix = np.diag(np.exp(-2j * np.atan(values)))
        print('unitary matrix:', unitary_matrix)
        self.oracle = UnitaryGate(unitary_matrix)
