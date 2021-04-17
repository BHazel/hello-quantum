import cirq
from cirq.value import big_endian_bits_to_int

def generate_random_number():
    """Generates a random number between 0-15.

    Returns:
        int: A random number between 0-15.
    """
    # Allocate 4 qubits.
    qubits = cirq.LineQubit.range(4)

    # Set up circuit.
    # Apply Hadamard gate to all qubits.
    circuit = cirq.Circuit()
    for qubit in qubits:
        circuit.append(
            cirq.H(qubit)
        )
    
    # Measure all qubits.
    for i in range(4):
        circuit.append(
            cirq.measure(qubits[i], key=f'qubit{i}')
        )
    
    # Initialise simulator and run circuit.
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1)

    # Convert result as binary digits into integer.
    qubit_results = []
    for i in range(4):
        qubit_results.append(result.data[f'qubit{i}'][0])
    
    random_number = big_endian_bits_to_int(qubit_results)
    
    # Return random number.
    return random_number

print('*** Hello, Quantum! - Random Number Generator (Cirq) ***')

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