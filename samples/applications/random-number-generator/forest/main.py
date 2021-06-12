import time
from pyquil import Program, get_qc, list_quantum_computers
from pyquil.gates import *
from pyquil.api import local_forest_runtime

def generate_random_number():
    """Generates a random number between 0-15.

    Returns:
        int: A random number between 0-15.
    """
    # Initialise program.
    # Apply Hadamard gate to 4 qubits.
    program = Program()
    for qubit in range(4):
        program += H(qubit)

    with local_forest_runtime():
        # Initialise simulator and run circuit a specified number of times.
        # Get counts of qubit measurement results, which is a single result with 1 count.
        quantum_virtual_machine = get_qc('9q-square-qvm')
        qubit_result_counts = quantum_virtual_machine.run_and_measure(program, trials=1)

        # Convert result as binary digits into bit-string.
        result_bitstring = '0b'
        for result in range(4):
            result_bitstring += str(qubit_result_counts[result][0])

        # Convert bit-string as binary digits into integer.
        random_number = int(result_bitstring, 2)
        return random_number

print('*** Hello, Quantum! - Random Number Generator (Forest) ***')

repeat_count = 10
random_numbers = []

# Repeat random number generation a specified number of times.
for i in range(repeat_count):
    random_number = generate_random_number()
    random_numbers.append(random_number)

    # Pause for 1 second to allow for connection to quantum virtual machine to close.
    time.sleep(1)

# Print random numbers.
print(f'Random numbers from {repeat_count} repeats:')
for random_number in random_numbers:
    print(f'\t{random_number}')