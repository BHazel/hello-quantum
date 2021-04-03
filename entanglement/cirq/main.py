import cirq

print('*** Hello, Quantum! - Entanglement (Cirq) ***')

# Allocate qubits.
control_qubit = cirq.GridQubit(0, 0)
target_qubit = cirq.GridQubit(0, 1)

# Set up circuit.
# Apply Hadamard gate to the control qubit.
# Apply Controlled NOT gate to the target qubit using the control qubit.
# Measure the control qubit with a key of 'control_qubit'.
# Measure the target qubit with a key of 'target_qubit'.
circuit = cirq.Circuit(
    cirq.H(control_qubit),
    cirq.CNOT(control_qubit, target_qubit),
    cirq.measure(control_qubit, key='control_qubit'),
    cirq.measure(target_qubit, key='target_qubit')
)

# Initialise simulator and run circuit a specified number of times.
repeat_count = 1000
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=repeat_count)

zero_zero_count = 0
zero_one_count = 0
one_zero_count = 0
one_one_count = 0

# Loop through results and update counts based on qubit measurement results.
for i in range(repeat_count):
    control_qubit_result = result.data['control_qubit'][i]
    target_qubit_result = result.data['target_qubit'][i]

    zero_zero_count += 1 if control_qubit_result == 0 and target_qubit_result == 0 else 0
    zero_one_count += 1 if control_qubit_result == 0 and target_qubit_result == 1 else 0
    one_zero_count += 1 if control_qubit_result == 1 and target_qubit_result == 0 else 0
    one_one_count += 1 if control_qubit_result == 1 and target_qubit_result == 1 else 0

# Print results.
print(f"Counts for {repeat_count} repeats:")
print(f"\t00: {zero_zero_count}")
print(f"\t01: {zero_one_count}")
print(f"\t10: {one_zero_count}")
print(f"\t11: {one_one_count}")