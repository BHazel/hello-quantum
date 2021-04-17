import time
from pyquil import Program, get_qc, list_quantum_computers
from pyquil.gates import *
from pyquil.api import local_forest_runtime

def superposition(repeat_count, basis_measurement):
    """Creates a superposition and measures it using a specified basis a specified number of times.

    Args:
        repeat_count (int): The number of times to repeat the quantum program.
        basis_measurement (function): The function to perform the specified basis measurement with.

    Returns:
        int: The measurement count where the result is 1.
    """
    program = Program()
    program += H(0)
    basis_measurement(program, 0)

    with local_forest_runtime():
        # Initialise simulator and run circuit a specified number of times.
        quantum_virtual_machine = get_qc('9q-square-qvm')
        qubit_result_counts = quantum_virtual_machine.run_and_measure(program, trials=repeat_count)
        
        # Loop through results and update count if result is 1.
        ones_count = 0
        for result in qubit_result_counts[0]:
            if result == 1:
                ones_count += 1
        
        return ones_count

def measure_x(program, qubit):
    """Measures a specified qubit in the Hadamard (X) basis.

    Args:
        program (pyquil.quil.Program): The quantum program to apply the measurement to.
        qubit (int): The qubit to measure.
    """
    program += H(qubit)

def measure_z(program, qubit):
    """Measures a specified qubit in the Computational (Z) basis.

    Args:
        program (pyquil.quil.Program): The quantum program to apply the measurement to.
        qubit (int): The qubit to measure.
    """
    pass

print('*** Hello, Quantum! - Measurement Bases (Forest) ***')

repeat_count = 1000

# Create and measure a superposition in the Computational Basis (Z-Basis).
result_ones_count_computational = superposition(repeat_count, measure_z)

# Pause for 1 second to allow for connection to quantum virtual machine to close.
time.sleep(1)

# Create and measure a superposition in the Hadamard Basis (X-Basis).
result_ones_count_hadamard = superposition(repeat_count, measure_x)
        
# Print results.
print(f"Counts for {repeat_count} repeats in Computational Basis:")
print(f"\t0: {repeat_count - result_ones_count_computational}")
print(f"\t1: {result_ones_count_computational}")
print(f"Counts for {repeat_count} repeats in Hadamard Basis:")
print(f"\t0: {repeat_count - result_ones_count_hadamard}")
print(f"\t1: {result_ones_count_hadamard}")