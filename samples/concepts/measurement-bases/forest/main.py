from pyquil import Program, get_qc
from pyquil.gates import *
from pyquil.quilbase import Declare

def superposition(repeat_count, basis_measurement):
    """Creates a superposition and measures it using a specified basis a specified number of times.

    Args:
        repeat_count (int): The number of times to repeat the quantum program.
        basis_measurement (function): The function to perform the specified basis measurement with.

    Returns:
        int: The measurement count where the result is 1.
    """
    # Initialise program with classical bit register.
    program = Program(
        Declare('c', "BIT", 1),
    )

    program += H(0)
    basis_measurement(program, 0)
    program += MEASURE(0, 'c')
    program.wrap_in_numshots_loop(repeat_count)

    # Initialise simulator and run circuit a specified number of times.
    quantum_virtual_machine = get_qc('9q-square-qvm')
    qubit_result_counts = quantum_virtual_machine.run(
        quantum_virtual_machine
            .compile(program)).readout_data.get('c')
    
    # Loop through results and update count if result is 1.
    ones_count = 0
    for result in qubit_result_counts:
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

# Create and measure a superposition in the Hadamard Basis (X-Basis).
result_ones_count_hadamard = superposition(repeat_count, measure_x)
        
# Print results.
print(f"Counts for {repeat_count} repeats in Computational Basis:")
print(f"\t0: {repeat_count - result_ones_count_computational}")
print(f"\t1: {result_ones_count_computational}")
print(f"Counts for {repeat_count} repeats in Hadamard Basis:")
print(f"\t0: {repeat_count - result_ones_count_hadamard}")
print(f"\t1: {result_ones_count_hadamard}")