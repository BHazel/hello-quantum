import sys
from typing import Callable
from pytket import Circuit

# Load tket backend factory.
sys.path.append('../../../libraries')
from tket_backend_factory import get_tket_backend

# Get quantum backend from command-line arguments.
backend = get_tket_backend()

def interference(repeat_count: int, starting_state: int) -> dict[tuple[int, ...], int]:
    """Creates a superposition and applies interference on a qubit in a specified state a specified number of times.

    Args:
        repeat_count (int): The number of times to repeat the quantum circuit.
        starting_state (int): The state to set the qubit to prior to running the quantum circuit.

    Returns:
        dict[tuple[int, ...], int]: The measurement result counts.
    """
    # Set up quantum circuit with 1 qubit and 1 bit.
    # Set qubit to desired starting state.
    # If the starting state should be 1, apply the X gate.
    circuit = Circuit(1, 1)
    if starting_state == 1:
        circuit.X(0)
    
    # Apply Hadamard gate to create a superposition.
    circuit.H(0)

    # Apply Hadamard gate to cause interference to restore qubit to its starting state.
    circuit.H(0)

    # Measure the qubit and save the result into a classical bit.
    circuit.Measure(0, 0)

    # Initialise backend and run circuit a specified number of times.
    backend.compile_circuit(circuit)
    job = backend.process_circuit(circuit, n_shots=repeat_count)

    # Get counts of qubit measurement results.
    result_counts = backend.get_result(job).get_counts()
    return result_counts

print('*** Hello, Quantum! - Interference (tket) ***')

repeat_count = 1000

# Cause interference on a qubit starting in the 0 state.
result_counts_starting_state_0 = interference(repeat_count, 0)

# Cause interference on a qubit starting in the 1 state.
result_counts_starting_state_1 = interference(repeat_count, 1)

# Print results.
print(f"Counts for {repeat_count} repeats with starting state 0:")
print(f"\t0: {result_counts_starting_state_0[(0,)]}")
print(f"\t1: {result_counts_starting_state_0[(1,)]}")
print(f"Counts for {repeat_count} repeats with starting state 1:")
print(f"\t0: {result_counts_starting_state_1[(0,)]}")
print(f"\t1: {result_counts_starting_state_1[(1,)]}")