from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute

print('*** Hello, Quantum! - Entanglement (Qiskit) ***')

# Set quantum and classical bit registers.
repeat_count = 1000
q = QuantumRegister(2, 'q')
c = ClassicalRegister(2, 'c')

# Set up cirbuit with quantum and classical bit registers.
# Apply Hadamard gate to the control qubit 0.
# Apply Controlled NOT gate to the target qubit 1 using qubit 0 as control.
# Measure the qubits and save the result into classical bits.
circuit = QuantumCircuit(q, c)
circuit.h(q[0])
circuit.cx(q[0], q[1])
circuit.measure(q, c)

# Initialise simulator and run circuit a specified number of times.
simulator = Aer.get_backend('qasm_simulator')
job = execute(circuit, simulator, shots=repeat_count)

# Get counts of qubit measurement results.
result_counts = job.result().get_counts()

# Print results.
print(f"Counts for {repeat_count} repeats:")
print(f"\t00: {result_counts.get('00', 0)}")
print(f"\t01: {result_counts.get('01', 0)}")
print(f"\t10: {result_counts.get('10', 0)}")
print(f"\t11: {result_counts.get('11', 0)}")