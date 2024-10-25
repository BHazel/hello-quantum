# Teleportation Mathematics

The _No-Cloning Theorem_ states that no quantum state can be cloned from one qubit onto another.  However, it is possible to transfer a state from one qubit to another as long as the original qubit loses its state in the process.  Due to the original state being lost this is therefore referred to as teleportation.

# Circuit Unitary Matrix & Statevector

As 3 qubits are involved in this circuit an $8\times8$ unitary matrix is required to represent it up to the two measurements.

To build the unitary matrix for the circuit each step ca be represented by its own 8$\times$8 unitary matrix, containing the operation on a specific qubit or qubits in a tensor product with the identity matrix for any qubits not affected at that step.  Stepping through the circuit above, the operations to build up the unitary matrix are shown in the table below.  The tensor products are each built up from the gates applied to the qubits in reverse order, i.e. from bottom to top in the circuit diagram.

Step | Operation
--- | ---
Initialise qubit $q_0$ to desired state to teleport, here $\|1\rangle$. | $I \otimes I \otimes X$
Apply the Hadamard gate to qubit $q_1$ and move it into superposition state $\|+\rangle$. | $I \otimes H \otimes I$
Entangle qubits $q_1$ and $q_2$ with the CNOT gate using qubit $q_1$ as control. | $CNOT \otimes I$
Entangle qubit $q_0$, containing the state to teleport, with the existing entangled state of qubits $q_1$ and $q_2$ with the CNOT gate using qubit $q_0$ as control. | $I \otimes CNOT$
Apply the Hadamard gate to qubit $q_0$. | $I \otimes I \otimes H$

Finally, the unitary matrix can be built by multiplying these operations together in reverse order.

$$
\begin{align*}
    M_i &= (I \otimes I \otimes H) \times (I \otimes CNOT) \times (CNOT \otimes I)\times (I \otimes H \otimes I) \times (I \otimes I \otimes X) \\
        &=
        \begin{bmatrix}
            0 & \frac{1}{2} & 0 & \frac{1}{2} & \frac{1}{2} & 0 & -\frac{1}{2} & 0\\[4pt]
            0 & \frac{1}{2} & 0 & \frac{1}{2} & -\frac{1}{2} & 0 & \frac{1}{2} & 0\\[4pt]
            \frac{1}{2} & 0 & \frac{1}{2} & 0 & 0 & \frac{1}{2} & 0 & -\frac{1}{2}\\[4pt]
            -\frac{1}{2} & 0 & -\frac{1}{2} & 0 & 0 & \frac{1}{2} & 0 & -\frac{1}{2}\\[4pt]
            \frac{1}{2} & 0 & -\frac{1}{2} & 0 & 0 & \frac{1}{2} & 0 & \frac{1}{2}\\[4pt]
            -\frac{1}{2} & 0 & \frac{1}{2} & 0 & 0 & \frac{1}{2} & 0 & \frac{1}{2}\\[4pt]
            0 & \frac{1}{2} & 0 & -\frac{1}{2} & \frac{1}{2} & 0 & \frac{1}{2} & 0\\[4pt]
            0 & \frac{1}{2} & 0 & -\frac{1}{2} & -\frac{1}{2} & 0 & -\frac{1}{2} & 0
        \end{bmatrix}
\end{align*}
$$

As the circuit is a 3-qubit system, its statevector will contain 8 possible states, all initially in the $|000\rangle$ state.  Multiplying this initial state, $|\psi\rangle$, by the unitary matrix, $M_i$, will give the statevector of the system prior to the measurement steps.

$$
M_i|\psi\rangle =
    M_i(|0_{q0}\rangle \otimes |0_{q1}\rangle \otimes |0_{q2}\rangle) =
    M_i \times
    \begin{bmatrix}
        1 \\[4pt] 0 \\[4pt] 0 \\[4pt] 0 \\[4pt] 0 \\[4pt] 0 \\[4pt] 0 \\[4pt] 0
    \end{bmatrix} =
    \begin{bmatrix}
        0 \\[4pt] 0 \\[4pt] \frac{1}{2} \\[4pt] -\frac{1}{2} \\[4pt] \frac{1}{2} \\[4pt] -\frac{1}{2} \\[4pt] 0 \\[4pt] 0
    \end{bmatrix}
$$