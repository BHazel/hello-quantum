from pyquil import Program, get_qc
from pyquil.gates import *
from pyquil.quilbase import Declare

print('*** Hello, Quantum! - Superposition (Forest) ***')

# Initialise program with classical bit register.
# Apply Hadamard gate to create a superposition.
repeat_count = 1000
program = Program(
    Declare('c', "BIT", 1),
    H(0),
    MEASURE(0, 'c')
).wrap_in_numshots_loop(repeat_count)

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

# Print results.
print(f"Counts for {repeat_count} repeats:")
print(f"\t0: {repeat_count - ones_count}")
print(f"\t1: {ones_count}")