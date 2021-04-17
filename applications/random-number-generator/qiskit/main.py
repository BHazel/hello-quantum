from qiskit import QuantumCircuit, Aer, execute

def generate_random_number():
    """Generates a random number between 0-15.

    Returns:
        int: A random number between 0-15.
    """
    # Set up quantum circuit with 4 qubits.
    circuit = QuantumCircuit(4)

    # Apply Hadamard gate to all qubits.
    for qubit in range(4):
        circuit.h(qubit)
    
    # Measure all qubits.
    circuit.measure_all()

    # Initialise simulator and run circuit.
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, simulator, shots=1)

    # Get counts of qubit measurement results, which is a single result with 1 count.
    # Convert result as binary digits into integer.
    result_counts = job.result().get_counts()
    random_number_bitstring = list(result_counts.keys())[0]
    random_number = int(f'0b{random_number_bitstring}', 2)

    # Return random number.
    return random_number

print('*** Hello, Quantum! - Random Number Generator (Qiskit) ***')

repeat_count = 10
random_numbers = []

# Repeat random number generation a specified number of times.
for i in range(repeat_count):
    random_number = generate_random_number()
    random_numbers.append(random_number)

# Print random numbers.
print(f'Random numbers from {repeat_count} repeats:')
for random_number in random_numbers:
    print(f'\t{random_number}')