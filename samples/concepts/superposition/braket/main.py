from timeit import repeat
from braket.devices import LocalSimulator
from braket.circuits import Circuit

print('*** Hello, Quantum! - Superposition (Braket) ***')

repeat_count = 1000

# Set up quantum circuit.
# Apply Hadamard gate to create a superpoition.
program = Circuit()
program.h(0)

# Initialise simulator and run circuit a specified number of times.
local_simulator = LocalSimulator()
result = local_simulator.run(program, shots=repeat_count).result()

# Get counts of qubit measurement results.
counts = result.measurement_counts

# Print results.
print(counts)