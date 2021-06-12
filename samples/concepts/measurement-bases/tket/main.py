import sys
from typing import Callable
from pytket import Circuit

# Load tket backend factory.
sys.path.append('../../../libraries')
from tket_backend_factory import get_tket_backend

# Get quantum backend from command-line arguments.
backend = get_tket_backend()

def superposition(repeat_count: int, basis_measurement: Callable[[Circuit, int, int], None]) -> dict[tuple[int, ...], int]:
    """Creates a superposition and measures it using a specified basis a specified number of times.

    Args:
        repeat_count (int): The number of times to repeat the quantum circuit.
        basis_measurement (Callable[[Circuit, int, int], None]): The function to perform the specified basis measurement with.

    Returns:
        dict[tuple[int, ...], int]: The measurement result counts.
    """
    # Set up quantum circuit with 1 qubit and 1 bit.
    # Apply Hadamard gate to qubit 0.
    # Measure qubit 0 into bit 0 using the specified measurement basis.
    circuit = Circuit(1, 1)
    circuit.H(0)
    basis_measurement(circuit, 0, 0)

    # Initialise backend and run circuit a specified number of times.
    backend.compile_circuit(circuit)
    job = backend.process_circuit(circuit, n_shots=repeat_count)

    # Get counts of qubit measurement results.
    result_counts = backend.get_result(job).get_counts()
    return result_counts

def measure_x(quantum_circuit: Circuit, qubit: int, bit: int) -> None:
    """Measures a specified qubit in the Hadamard (X) basis.

    Args:
        quantum_circuit (pytket.circuit.Circuit): The quantum circuit to apply the measurement to.
        qubit (int): The qubit to measure.
        bit (int): The bit to save the qubit measurement result into.
    """
    # Apply Hadamard gate to the qubit.
    # Measure the qubit into the bit.
    quantum_circuit.H(qubit)
    quantum_circuit.Measure(qubit, bit)

def measure_z(quantum_circuit: Circuit, qubit: int, bit: int) -> None:
    """Measures a specified qubit in the Computational (Z) basis.

    Args:
        quantum_circuit (pytket.circuit.Circuit): The quantum circuit to apply the measurement to.
        qubit (int): The qubit to measure.
        bit (int): The bit to save the qubit measurement result into.
    """
    # Measure the qubit into the bit.
    quantum_circuit.Measure(qubit, bit)

print('*** Hello, Quantum! - Measurement Bases (tket) ***')

repeat_count = 1000

# Create and measure a superposition in the Computational Basis (Z-Basis).
result_counts_computational = superposition(repeat_count, measure_z)

# Create and measure a superposition in the Hadamard Basis (X-Basis).
result_counts_hadamard = superposition(repeat_count, measure_x)

# Print results.
print(f"Counts for {repeat_count} repeats in Computational Basis:")
print(f"\t0: {result_counts_computational[(0,)]}")
print(f"\t1: {result_counts_computational[(1,)]}")
print(f"Counts for {repeat_count} repeats in Hadamard Basis:")
print(f"\t0: {result_counts_hadamard[(0,)]}")
print(f"\t1: {result_counts_hadamard[(1,)]}")