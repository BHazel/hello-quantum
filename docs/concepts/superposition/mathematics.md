# Superposition Mathematics

To move a qubit in one of the computational basis states into superposition, apply the Hadamard gate. Like all other single-qubit gates it is a $2\times2$ unitary matrix.

$$
    H = \frac{1}{\sqrt{2}}
    \begin{bmatrix}
        1 & 1 \\ 1 & -1
    \end{bmatrix}
$$

Applying this to the computational basis states creates a superposition with a 1:1 combination of $|0\rangle$ and $|1\rangle$.

$$
    H|0\rangle =
    H\begin{bmatrix}
        1 \\[4pt] 0
    \end{bmatrix} =
    \frac{1}{\sqrt{2}}
    \begin{bmatrix}
        1 & 1 \\[4pt] 1 & -1
    \end{bmatrix}
    \begin{bmatrix}
        1 \\[4pt] 0
    \end{bmatrix} =
    \begin{bmatrix}
        \frac{1}{\sqrt{2}} \\[4pt] \frac{1}{\sqrt{2}}
    \end{bmatrix} =
    \frac{1}{\sqrt{2}} \begin{bmatrix}
        1 \\[4pt] 1
    \end{bmatrix}
$$

$$
    H|1\rangle =
    H\begin{bmatrix}
        0 \\[4pt] 1
    \end{bmatrix} =
    \frac{1}{\sqrt{2}}
    \begin{bmatrix}
        1 & 1 \\[4pt] 1 & -1
    \end{bmatrix}
    \begin{bmatrix}
        0 \\[4pt] 1
    \end{bmatrix} =
    \begin{bmatrix}
        \frac{1}{\sqrt{2}} \\[4pt] -\frac{1}{\sqrt{2}}
    \end{bmatrix} =
    \frac{1}{\sqrt{2}} \begin{bmatrix}
        1 \\[4pt] -1
    \end{bmatrix}
$$

These matrix forms of the states can be written in Dirac notation:

$$
    H|0\rangle =
    \frac{1}{\sqrt{2}} \begin{bmatrix}
        1 \\ 1
    \end{bmatrix} =
    \frac{1}{\sqrt{2}} \left(\begin{bmatrix}
        1 \\ 0
    \end{bmatrix} +
    \begin{bmatrix}
        0 \\ 1
    \end{bmatrix}\right) =
    \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)
$$

$$
    H|1\rangle =
    \frac{1}{\sqrt{2}} \begin{bmatrix}
        1 \\ -1
    \end{bmatrix} =
    \frac{1}{\sqrt{2}} \left(\begin{bmatrix}
        1 \\ 0
    \end{bmatrix} -
    \begin{bmatrix}
        0 \\ 1
    \end{bmatrix}\right) =
    \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)
$$

These states are so common, and also form the basis states of the Hadamard (X) basis, they have short-hand kets in Dirac notation of $|+\rangle$ and $|-\rangle$ as well:

$$
    H|0\rangle =
    \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) =
    |+\rangle
$$

$$
    H|1\rangle =
    \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) =
    |-\rangle
$$