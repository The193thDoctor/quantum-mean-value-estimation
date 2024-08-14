import abc
from qiskit import  QuantumCircuit, QuantumRegister, AncillaRegister
import numpy as np


class BaseOracle(abc.ABC):
    def __init__(self, num_qubits):
        self.oracle = None
        self.num_qubits = num_qubits
        self.num_ancillas = None

    @abc.abstractmethod
    def set_oracle(self, values):
        pass


class RyanOracle(BaseOracle):
    def __init__(self, num_qubits, input_dimension=1):
        super().__init__(num_qubits)
        self.num_ancillas = 0
        if input_dimension != 1:
            ValueError('Input dimension must be 1')

    def set_oracle(self, values):
        if len(values) != 1:
            ValueError('Input values must be of length 1')
        num_values = 2 ** self.num_qubits
        if len(values) > num_values:
            ValueError('Too many input values')
        values = np.pad(values, (0, num_values - len(values)), 'constant')
        unitary_matrix = np.diag(np.exp(-2j * np.atan(values)))

        qr = QuantumRegister(self.num_qubits, 'q')
        anc = AncillaRegister(self.num_ancillas, 'anc')
        self.oracle = QuantumCircuit(qr, anc)
        self.oracle.unitary(unitary_matrix, qr)


class SearchOracle(BaseOracle):
    def __init__(self, num_qubits, input_dimension=1):
        super().__init__(num_qubits)
        self.num_ancillas = 0
        if input_dimension != 1:
            ValueError('Input dimension must be 1')

    def set_oracle(self, values):
        if len(values) != 1:
            ValueError('Input values must be of length 1')
        num_values = 2 ** self.num_qubits
        if len(values) > num_values:
            ValueError('Too many input values')
        values = np.pad(values, (0, num_values - len(values)), 'constant')
        unitary_matrix = np.diag(np.power(-1, np.logical_not(np.isclose(values, 0))))

        qr = QuantumRegister(self.num_qubits, 'q')
        anc = AncillaRegister(self.num_ancillas, 'anc')
        self.oracle = QuantumCircuit(qr, anc)
        self.oracle.unitary(unitary_matrix, qr)