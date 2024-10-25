from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute

def teleport(defer_measurement: bool):
    state_to_teleport = 0
    alice = 1
    bob = 2

    q = QuantumRegister(3, 'q')
    c = ClassicalRegister(3, 'c')

    circuit = QuantumCircuit(q, c)
    circuit.x(q[state_to_teleport])
    circuit.h(q[alice])
    circuit.cx(q[alice], q[bob])
    circuit.cx(q[state_to_teleport], q[alice])
    circuit.h(q[state_to_teleport])

    if defer_measurement == True:
        circuit.cx(q[alice], q[bob])
        circuit.cz(q[state_to_teleport], q[bob])
        #circuit.measure([0, 1, 2], [0, 1, 2])
        circuit.measure(2, 0)
    else:
        circuit.measure(q[state_to_teleport], c[state_to_teleport])
        circuit.measure(q[alice], c[alice])

        if c[alice] == 1:
            circuit.x(q[bob])
        
        if c[state_to_teleport] == 1:
            circuit.z(q[bob])
        
        circuit.measure(q[bob], c[bob])

    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, simulator, shots=1000)
    result = job.result()
    print(result.get_counts())

teleport(True)