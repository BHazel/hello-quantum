import cirq

print('*** Hello, Quantum! - Superposition (Cirq) ***')

# Allocate qubit.
qubit = cirq.GridQubit(0, 0)

# Set up circuit.
# Apply Hadamard gate to create a superposition.
# Measure the qubit with key of 'qubit'.
circuit = cirq.Circuit(
    cirq.H(qubit),
    cirq.measure(qubit, key='qubit')
)

# Initialise simulator and run circuit a specified number of times.
repeat_count = 1000
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=repeat_count)

# Get count of qubit measurements where result is 1.
ones_count = result.data[result.data == 1].count().qubit

# Print results.
print(f"Counts for {repeat_count} repeats:")
print(f"\t0: {repeat_count - ones_count}")
print(f"\t1: {ones_count}")