import sys
from pytket import Circuit

# Load tket backend factory.
sys.path.append('../../../libraries')
from tket_backend_factory import get_tket_backend

# Get quantum backend from command-line arguments.
backend = get_tket_backend()

print('*** Hello, Quantum! - Entanglement (tket) ***')

repeat_count = 1000

# Set up cirbuit with 2 qubits and 2 classical bits.
# Apply Hadamard gate to the control qubit 0.
# Apply Controlled NOT gate to the target qubit 1 using qubit 0 as control.
# Measure the qubits and save the result into classical bits.
circuit = Circuit(2, 2)
circuit.H(0)
circuit.CX(0, 1)
circuit.Measure(0, 0)
circuit.Measure(1, 1)

# Initialise backend and run circuit a specified number of times.
backend.compile_circuit(circuit)
job = backend.process_circuit(circuit, n_shots=repeat_count)

# Get counts of qubit measurement results.
result_counts = backend.get_result(job).get_counts()

# Print results.
print(f"Counts for {repeat_count} repeats:")
print(f"\t00: {result_counts[(0, 0)]}")
print(f"\t01: {result_counts[(0, 1)]}")
print(f"\t10: {result_counts[(1, 0)]}")
print(f"\t11: {result_counts[(1, 1)]}")