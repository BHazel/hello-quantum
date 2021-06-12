import sys
from typing import Callable
from pytket import Circuit

# Load tket backend factory.
sys.path.append('../../../libraries')
from tket_backend_factory import get_tket_backend

# Get quantum backend from command-line arguments.
backend = get_tket_backend()

def generate_random_number() -> int:
    """Generates a random number between 0-15.

    Returns:
        int: A random number between 0-15.
    """
    # Set up quantum circuit with 4 qubits.
    circuit = Circuit(4, 4)

    # Apply Hadamard gate to all qubits.
    for qubit in range(4):
        circuit.H(qubit)

    # Measure all qubits.
    circuit.measure_all()

    # Initialise simulator and run circuit.
    job = backend.process_circuit(circuit, n_shots=1)
    shots = backend.get_result(job).get_shots()

    # Get shot measurement results and convert result as binary digits into integer.
    random_number_bitstring = ''.join(list(map(str, shots[0])))
    random_number = int(f'0b{random_number_bitstring}', 2)
    return random_number

print('*** Hello, Quantum! - Random Number Generator (tket) ***')

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