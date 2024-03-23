import numpy as np
from qiskit_aer.noise import NoiseModel, errors
from qiskit.quantum_info.operators import Operator

def get_secret_noise_model():
    # Create the noise model
    noise_model = NoiseModel()

    # Add readout error
    readout_error = errors.readout_error.ReadoutError([[0.99, 0.01], [0.05, 0.95]])
    noise_model.add_all_qubit_readout_error(readout_error)

    # Add coherent error
    unitary_operator = Operator([[1, 0],[0, np.exp(1j*0.001)]])
    error_gate = errors.coherent_unitary_error(unitary_operator)
    noise_model.add_all_qubit_quantum_error(error_gate, ['rz', 'sx'], warnings=False)

    # Add depolarizing error
    depolarizing_error = errors.depolarizing_error(0.005, 2)
    noise_model.add_all_qubit_quantum_error(depolarizing_error, "cx")