from pyquil import Program, get_qc
from pyquil.gates import *
from pyquil.quilbase import Declare

def interference(repeat_count, starting_state):
    """Creates a superposition and applies interference on a qubit in a specified state a specified number of times.

    Args:
        repeat_count (int): The number of times to repeat the quantum circuit.
        starting_state (int): The state to set the qubit to prior to running the quantum circuit.

    Returns:
        int: The measurement count where the result is 1.
    """
    # Initialise program with classical bit register.
    program = Program(
        Declare('c', "BIT", 1)
    )

    # Set qubit to desired starting state.
    # If the starting state should be 1, apply the X gate.
    if starting_state == 1:
        program += X(0)
    
    # Apply Hadamard gate to create a superposition.
    program += H(0)

    # Apply Hadamard gate to cause interference to restore qubit to its starting state.
    program += H(0)
    program += MEASURE(0, 'c')
    program.wrap_in_numshots_loop(repeat_count)

    # Initialise simulator and run circuit a specified number of times.
    quantum_virtual_machine = get_qc('9q-square-qvm')
    qubit_result_counts = quantum_virtual_machine.run(
        quantum_virtual_machine
            .compile(program)).readout_data.get('c')
    
    # Loop through results and update count if result is 1.
    ones_count = 0
    for result in qubit_result_counts:
        if result == 1:
            ones_count += 1
    
    return ones_count

print('*** Hello, Quantum! - Interference (Forest) ***')

repeat_count = 1000

# Cause interference on a qubit starting in the 0 state.
result_counts_starting_state_0 = interference(repeat_count, 0)

# Cause interference on a qubit starting in the 1 state.
result_counts_starting_state_1 = interference(repeat_count, 1)

# Print results.
print(f"Counts for {repeat_count} repeats with starting state 0:")
print(f"\t0: {repeat_count - result_counts_starting_state_0}")
print(f"\t1: {result_counts_starting_state_0}")
print(f"Counts for {repeat_count} repeats with starting state 1:")
print(f"\t0: {repeat_count - result_counts_starting_state_1}")
print(f"\t1: {result_counts_starting_state_1}")