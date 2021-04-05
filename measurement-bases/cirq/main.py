import cirq

def superposition(repeat_count, basis_measurement, qubit_key):
    """Creates a superposition and measures it using a specified basis a specified number of times.

    Args:
        repeat_count (int): The number of times to repeat the quantum program.
        basis_measurement (function): The function to perform the specified basis measurement with.
        qubit_key (str): The identifier for the qubit when measured.

    Returns:
        int: The measurement count where the result is 1.
    """
    # Allocate qubit.
    qubit = cirq.GridQubit(0, 0)

    # Set up circuit.
    # Apply Hadamard gate to create a superposition.
    circuit = cirq.Circuit(
        cirq.H(qubit)
    )
    
    basis_measurement(circuit, qubit, qubit_key)

    # Initialise simulator and run circuit a specified number of times.
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=repeat_count)

    # Get count of qubit measurements where result is 1.
    ones_count = result.data[result.data == 1].count()[qubit_key]
    return ones_count

def measure_x(circuit, qubit, qubit_key):
    """Measures a specified qubit in the Hadamard (X) basis.

    Args:
        program (cirq.Circuit): The quantum circuit to apply the measurement to.
        qubit (cirq.GridQubit): The qubit to measure.
        qubit_key (str): The identifier for the qubit when measured.
    """
    circuit.append([
        cirq.H(qubit),
        cirq.measure(qubit, key=qubit_key)
    ])

def measure_z(circuit, qubit, qubit_key):
    """Measures a specified qubit in the Computational (Z) basis.

    Args:
        program (cirq.Circuit): The quantum circuit to apply the measurement to.
        qubit (cirq.GridQubit): The qubit to measure.
        qubit_key (str): The identifier for the qubit when measured.
    """
    circuit.append(
        cirq.measure(qubit, key=qubit_key)
    )

print('*** Hello, Quantum! - Measurement Bases (Cirq) ***')

repeat_count = 1000

# Create and measure a superposition in the Computational Basis (Z-Basis).
result_ones_count_computational = superposition(repeat_count, measure_z, 'qubit_z')

# Create and measure a superposition in the Hadamard Basis (X-Basis).
result_ones_count_hadamard = superposition(repeat_count, measure_x, 'qubit_x')

# Print results.
print(f"Counts for {repeat_count} repeats in Computational Basis:")
print(f"\t0: {repeat_count - result_ones_count_computational}")
print(f"\t1: {result_ones_count_computational}")
print(f"Counts for {repeat_count} repeats in Hadamard Basis:")
print(f"\t0: {repeat_count - result_ones_count_hadamard}")
print(f"\t1: {result_ones_count_hadamard}")