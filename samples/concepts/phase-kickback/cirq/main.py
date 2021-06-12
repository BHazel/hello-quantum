import cirq

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

print('*** Hello, Quantum! - Phase Kickback (Cirq) ***')

# Allocate qubits.
control_qubit = cirq.GridQubit(0, 0)
target_qubit = cirq.GridQubit(0, 1)

# Set up circuit.
circuit = cirq.Circuit(
    # Apply Hadamard gate to control qubit to create a superposition in the
    # (+)-superposition state.
    cirq.H(control_qubit),

    # Apply X gate to target qubit to set it to the 1 state.
    # Apply Hadamard gate to target qubit to create a superposition in the
    # (-)-superposition state.
    cirq.X(target_qubit),
    cirq.H(target_qubit),

    # Apply CNOT gate to target qubit using the control qubit to trigger phase
    # kickback onto the control qubit.
    cirq.CNOT(control_qubit, target_qubit)
)

# Measure qubits in the Hadamard (X) basis.
measure_x(circuit, control_qubit, 'control_qubit')
measure_x(circuit, target_qubit, 'target_qubit')

# Initialise simulator and run circuit a specified number of times.
repeat_count = 1000
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=repeat_count)

plus_plus_count = 0
plus_minus_count = 0
minus_plus_count = 0
minus_minus_count = 0

# Loop through results and update counts based on qubit measurement results.
for i in range(repeat_count):
    control_qubit_result = result.data['control_qubit'][i]
    target_qubit_result = result.data['target_qubit'][i]

    plus_plus_count += 1 if control_qubit_result == 0 and target_qubit_result == 0 else 0
    plus_minus_count += 1 if control_qubit_result == 0 and target_qubit_result == 1 else 0
    minus_plus_count += 1 if control_qubit_result == 1 and target_qubit_result == 0 else 0
    minus_minus_count += 1 if control_qubit_result == 1 and target_qubit_result == 1 else 0

# Print results.
print(f"Counts for {repeat_count} repeats:")
print(f"\t++: {plus_plus_count}")
print(f"\t+-: {plus_minus_count}")
print(f"\t-+: {minus_plus_count}")
print(f"\t--: {minus_minus_count}")