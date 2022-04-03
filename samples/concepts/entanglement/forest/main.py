from pyquil import Program, get_qc
from pyquil.gates import *
from pyquil.quilbase import Declare

print('*** Hello, Quantum! - Entanglement (Forest) ***')

# Initialise program with classical bit register.
# Apply Hadamard gate to the control qubit 0.
# Apply Controlled NOT gate to the target qubit 1 using qubit 0 as control.
repeat_count = 1000
program = Program(
    Declare('c', "BIT", 2),
    H(0),
    CNOT(0, 1),
    MEASURE(0, ('c', 0)),
    MEASURE(1, ('c', 1))
).wrap_in_numshots_loop(repeat_count)

# Initialise simulator and run circuit a specified number of times.
program.wrap_in_numshots_loop(repeat_count)
quantum_virtual_machine = get_qc('9q-square-qvm')
qubit_result_counts = quantum_virtual_machine.run(
    quantum_virtual_machine
        .compile(program)).readout_data.get('c')

zero_zero_count = 0
zero_one_count = 0
one_zero_count = 0
one_one_count = 0

# Loop through results and update counts based on qubit measurement results.
for i in range(repeat_count):
    control_qubit_result = qubit_result_counts[i][0]
    target_qubit_result = qubit_result_counts[i][1]

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