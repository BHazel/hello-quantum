import sys
from pytket import Circuit

# Load tket backend factory.
sys.path.append('../../../libraries')
from tket_backend_factory import get_tket_backend

# Get quantum backend from command-line arguments.
backend = get_tket_backend()

print('*** Hello, Quantum! - Superposition (tket) ***')

repeat_count = 1000

# Set up quantum circuit with 1 qubit and 1 bit.
# Apply Hadamard gate to create a superposition.
# Measure the qubit and save the result into a classical bit.
circuit = Circuit(1, 1)
circuit.H(0)
circuit.Measure(0, 0)

# Initialise backend and run circuit a specified number of times.
backend.compile_circuit(circuit)
job = backend.process_circuit(circuit, n_shots=repeat_count)

# Get counts of qubit measurement results.
result_counts = backend.get_result(job).get_counts()

# Print results.
print(f"Counts for {repeat_count} repeats:")
print(f"\t0: {result_counts[(0,)]}")
print(f"\t1: {result_counts[(1,)]}")