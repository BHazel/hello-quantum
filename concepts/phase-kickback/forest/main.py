from pyquil import Program, get_qc, list_quantum_computers
from pyquil.gates import *
from pyquil.api import local_forest_runtime

def measure_x(program, qubit):
    """Measures a specified qubit in the Hadamard (X) basis.

    Args:
        program (pyquil.quil.Program): The quantum program to apply the measurement to.
        qubit (int): The qubit to measure.
    """
    program += H(qubit)

print('*** Hello, Quantum! - Phase Kickback (Forest) ***')

# Initialise program.
program = Program()

# Apply Hadamard gate to control qubit to create a superposition in the
# (+)-superposition state.
program += H(0)

# Apply X gate to target qubit to set it to the 1 state.
# Apply Hadamard gate to target qubit to create a superposition in the
# (-)-superposition state.
program += X(1)
program += H(1)

# Apply CNOT gate to target qubit using the control qubit to trigger phase
# kickback onto the control qubit.
program += CNOT(0, 1)

# Measure qubits in the Hadamard (X) basis.
measure_x(program, 0)
measure_x(program, 1)

repeat_count = 1000
with local_forest_runtime():
    # Initialise simulator and run circuit a specified number of times.
    quantum_virtual_machine = get_qc('9q-square-qvm')
    qubit_result_counts = quantum_virtual_machine.run_and_measure(program, trials=repeat_count)

    plus_plus_count = 0
    plus_minus_count = 0
    minus_plus_count = 0
    minus_minus_count = 0

    # Loop through results and update counts based on qubit measurement results.
    for i in range(repeat_count):
        control_qubit_result = qubit_result_counts[0][i]
        target_qubit_result = qubit_result_counts[1][i]

        plus_plus_count += 1 if control_qubit_result == 0 and target_qubit_result == 0 else 0
        plus_minus_count += 1 if control_qubit_result == 0 and target_qubit_result == 1 else 0
        minus_plus_count += 1 if control_qubit_result == 1 and target_qubit_result == 0 else 0
        minus_minus_count += 1 if control_qubit_result == 1 and target_qubit_result == 1 else 0

    # Print results.
    print(f"Counts for {repeat_count} repeats:")
    print(f"\t++: {plus_plus_count}")
    print(f"\t+-: {plus_minus_count}")
    print(f"\t-+: {minus_plus_count}")
    print(f"\t--: {minus_minus_count}")