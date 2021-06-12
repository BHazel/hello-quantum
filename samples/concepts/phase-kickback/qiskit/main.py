from qiskit import QuantumCircuit, Aer, execute

def measure_x(quantum_circuit: QuantumCircuit, qubit: int, bit: int) -> None:
    """Measures a specified qubit in the Hadamard (X) basis.

    Args:
        quantum_circuit (qiskit.circuit.quantumcircuit.QuantumCircuit): The quantum circuit to apply the measurement to.
        qubit (int): The qubit to measure.
        bit (int): The bit to save the qubit measurement result into.
    """
    quantum_circuit.h(qubit)
    quantum_circuit.measure(qubit, bit)

print('*** Hello, Quantum! - Phase Kickback (Qiskit) ***')

# Set quantum and classical bit registers.
repeat_count = 1000
circuit = QuantumCircuit(2, 2)

# Apply Hadamard gate to control qubit to create a superposition in the
# (+)-superposition state.
circuit.h(0)

# Apply X gate to target qubit to set it to the 1 state.
# Apply Hadamard gate to target qubit to create a superposition in the
# (-)-superposition state.
circuit.x(1)
circuit.h(1)

# Apply CNOT gate to target qubit using the control qubit to trigger phase
# kickback onto the control qubit.
circuit.cx(0, 1)

# Measure qubits in the Hadamard (X) basis.
measure_x(circuit, 0, 0)
measure_x(circuit, 1, 1)

# Initialise simulator and run circuit a specified number of times.
simulator = Aer.get_backend('qasm_simulator')
job = execute(circuit, simulator, shots=repeat_count)

# Get counts of qubit measurement results.
result_counts = job.result().get_counts()

# Print results.
print(f"Counts for {repeat_count} repeats:")
print(f"\t++: {result_counts.get('00', 0)}")
print(f"\t+-: {result_counts.get('01', 0)}")
print(f"\t-+: {result_counts.get('10', 0)}")
print(f"\t--: {result_counts.get('11', 0)}")