import cirq

def interference(repeat_count, starting_state, qubit_key):
    """Creates a superposition and applies interference on a qubit in a specified state a specified number of times.

    Args:
        repeat_count (int): The number of times to repeat the quantum circuit.
        starting_state (int): The state to set the qubit to prior to running the quantum circuit.
        qubit_key (str): The identifier for the qubit when measured.

    Returns:
        int: The measurement count where the result is 1.
    """
    # Allocate qubit.
    qubit = cirq.GridQubit(0, 0)

    # Set up circuit.
    # Set qubit to desired starting state.
    # If the starting state should be 1, apply the X gate.
    circuit = cirq.Circuit()
    if starting_state == 1:
        circuit.append(
            cirq.X(qubit)
        )
    
    circuit.append([
        # Apply Hadamard gate to create a superposition.
        cirq.H(qubit),

        # Apply Hadamard gate to cause interference to restore qubit to its starting state.
        cirq.H(qubit),

        # Measure the qubit with the specified key.
        cirq.measure(qubit, key=qubit_key)
    ])

    # Initialise simulator and run circuit a specified number of times.
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=repeat_count)

    # Get count of qubit measurements where result is 1.
    ones_count = result.data[result.data == 1].count()[qubit_key]
    return ones_count

print('*** Hello, Quantum! - Interference (Cirq) ***')

repeat_count = 1000

# Cause interference on a qubit starting in the 0 state.
result_counts_starting_state_0 = interference(repeat_count, 0, 'qubit_0')

# Cause interference on a qubit starting in the 1 state.
result_counts_starting_state_1 = interference(repeat_count, 1, 'qubit_1')

# Print results.
print(f"Counts for {repeat_count} repeats with starting state 0:")
print(f"\t0: {repeat_count - result_counts_starting_state_0}")
print(f"\t1: {result_counts_starting_state_0}")
print(f"Counts for {repeat_count} repeats with starting state 1:")
print(f"\t0: {repeat_count - result_counts_starting_state_1}")
print(f"\t1: {result_counts_starting_state_1}")