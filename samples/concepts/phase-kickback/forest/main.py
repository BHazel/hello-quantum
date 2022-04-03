from pyquil import Program, get_qc
from pyquil.gates import *
from pyquil.quilbase import Declare

print('*** Hello, Quantum! - Phase Kickback (Forest) ***')

# Initialise program with classical bit register.
repeat_count = 1000
program = Program()
program += Declare('c', 'BIT', 2)

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
program += H(0)
program += H(1)
program += MEASURE(0, ('c', 0))
program += MEASURE(1, ('c', 1))

# Initialise simulator and run circuit a specified number of times.
program.wrap_in_numshots_loop(repeat_count)
quantum_virtual_machine = get_qc('9q-square-qvm')
qubit_result_counts = quantum_virtual_machine.run(
    quantum_virtual_machine
        .compile(program)).readout_data.get('c')

plus_plus_count = 0
plus_minus_count = 0
minus_plus_count = 0
minus_minus_count = 0

# Loop through results and update counts based on qubit measurement results.
for i in range(repeat_count):
    control_qubit_result = qubit_result_counts[i][0]
    target_qubit_result = qubit_result_counts[i][1]

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