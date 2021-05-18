import sys
from pytket import Circuit

# Load tket backend factory.
sys.path.append('../../../libraries')
from tket_backend_factory import get_tket_backend

# Get quantum backend from command-line arguments.
backend = get_tket_backend()

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

print('*** Hello, Quantum! - Phase Kickback (tket) ***')

repeat_count = 1000

# Set up cirbuit with 2 qubits and 2 classical bits.
circuit = Circuit(2, 2)

# Apply Hadamard gate to control qubit to create a superposition in the
# (+)-superposition state.
circuit.H(0)

# Apply X gate to target qubit to set it to the 1 state.
# Apply Hadamard gate to target qubit to create a superposition in the
# (-)-superposition state.
circuit.X(1)
circuit.H(1)

# Apply CNOT gate to target qubit using the control qubit to trigger phase
# kickback onto the control qubit.
circuit.CX(0, 1)

# Measure qubits in the Hadamard (X) basis.
measure_x(circuit, 0, 0)
measure_x(circuit, 1, 1)

# Initialise backend and run circuit a specified number of times.
backend.compile_circuit(circuit)
job = backend.process_circuit(circuit, n_shots=repeat_count)

# Get counts of qubit measurement results.
result_counts = backend.get_result(job).get_counts()

# Print results.
print(f"Counts for {repeat_count} repeats:")
print(f"\t++: {result_counts[(0, 0)]}")
print(f"\t+-: {result_counts[(0, 1)]}")
print(f"\t-+: {result_counts[(1, 0)]}")
print(f"\t--: {result_counts[(1, 1)]}")