from pyquil import Program, get_qc, list_quantum_computers
from pyquil.gates import *
from pyquil.api import local_forest_runtime

print('*** Hello, Quantum! - Entanglement (Forest) ***')

# Initialise program.
# Apply Hadamard gate to the control qubit 0.
# Apply Controlled NOT gate to the target qubit 1 using qubit 0 as control.
program = Program()
program += H(0)
program += CNOT(0, 1)

repeat_count = 1000
with local_forest_runtime():
    # Initialise simulator and run circuit a specified number of times.
    quantum_virtual_machine = get_qc('9q-square-qvm')
    qubit_result_counts = quantum_virtual_machine.run_and_measure(program, trials=repeat_count)

    zero_zero_count = 0
    zero_one_count = 0
    one_zero_count = 0
    one_one_count = 0

    # Loop through results and update counts based on qubit measurement results.
    for i in range(repeat_count):
        control_qubit_result = qubit_result_counts[0][i]
        target_qubit_result = qubit_result_counts[1][i]

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