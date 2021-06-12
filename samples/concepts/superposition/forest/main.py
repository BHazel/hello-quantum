from pyquil import Program, get_qc, list_quantum_computers
from pyquil.gates import *
from pyquil.api import local_forest_runtime

print('*** Hello, Quantum! - Superposition (Forest) ***')

# Initialise program.
# Apply Hadamard gate to create a superposition.
program = Program()
program += H(0)

repeat_count = 1000
with local_forest_runtime():
    # Initialise simulator and run circuit a specified number of times.
    quantum_virtual_machine = get_qc('9q-square-qvm')
    qubit_result_counts = quantum_virtual_machine.run_and_measure(program, trials=repeat_count)
    
    # Loop through results and update count if result is 1.
    ones_count = 0
    for result in qubit_result_counts[0]:
        if result == 1:
            ones_count += 1
        
    # Print results.
    print(f"Counts for {repeat_count} repeats:")
    print(f"\t0: {repeat_count - ones_count}")
    print(f"\t1: {ones_count}")