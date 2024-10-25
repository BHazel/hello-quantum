# Interference Mathematics

As shown on the [Superposition Mathematics](../superposition/mathematics.md) page, if you apply the Hadamard gate to a qubit in the computational basis it creates a superposition with a 1:1 combination between $|0\rangle$ and $|1\rangle$.  When the qubit is measured in that superposition state it has a 50% probability of collapsing to $|0\rangle$ and the remaining 50% probability of collapsing to $|1\rangle$.  However, if the qubit is not measured and the Hadamard gate applied again, the qubit is returned to its original computational basis state.  This is due to quantum interference.

## Matrix Notation

Each quantum gate is represented by a square matrix which is its own inverse, hence each quantum gate is reversible.

\[
    H|+\rangle =
    \left(
        \frac{1}{\sqrt{2}}
        \begin{bmatrix}
            1 & 1 \\[4pt] 1 & -1
        \end{bmatrix}
    \right)
    \left(
        \frac{1}{\sqrt{2}}
        \begin{bmatrix}
            1 \\[4pt] 1
        \end{bmatrix}
    \right) =
    \frac{1}{2}
    \begin{bmatrix}
        1 & 1 \\[4pt] 1 & -1
    \end{bmatrix}
    \begin{bmatrix}
        1 \\[4pt] 1
    \end{bmatrix} =
    \frac{1}{2}
    \begin{bmatrix}
        1 + 1 \\[4pt] 1 - 1
    \end{bmatrix} =
    \begin{bmatrix}
        1 \\[4pt] 0
    \end{bmatrix} =
    |0\rangle
\]

\[
    H|-\rangle =
    \left(
        \frac{1}{\sqrt{2}}
        \begin{bmatrix}
            1 & 1 \\[4pt] 1 & -1
        \end{bmatrix}
    \right)
    \left(
        \frac{1}{\sqrt{2}}
        \begin{bmatrix}
            1 \\[4pt] -1
        \end{bmatrix}
    \right) =
    \frac{1}{2}
    \begin{bmatrix}
        1 & 1 \\[4pt] 1 & -1
    \end{bmatrix}
    \begin{bmatrix}
        1 \\[4pt] -1
    \end{bmatrix} =
    \frac{1}{2}
    \begin{bmatrix}
        1 - 1 \\[4pt] 1 + 1
    \end{bmatrix} =
    \begin{bmatrix}
        0 \\[4pt] 1
    \end{bmatrix} =
    |1\rangle
\]

## Dirac Notation

This approach works directly with the ket forms of the states and clearly demonstrates how the process works via quantum interference.  Instead of applying a matrix, in this notation the Hadamard gate is applied to each component of the superposition.

\begin{align*}
    H|+\rangle &= H\left(\frac{1}{\sqrt{2}}\left(|0\rangle + |1\rangle\right)\right) \\
               &= \frac{1}{\sqrt{2}}\left(H|0\rangle + H|1\rangle\right) \\
               &= \frac{1}{\sqrt{2}}\left(\frac{1}{\sqrt{2}}\left(|0\rangle + |1\rangle\right) + H|1\rangle\right) \\
               &= \frac{1}{\sqrt{2}}\left(\frac{1}{\sqrt{2}}\left(|0\rangle + |1\rangle\right) + \frac{1}{\sqrt{2}}\left(|0\rangle - |1\rangle\right)\right) \\
               &= \frac{1}{\sqrt{2}}\left(\frac{1}{\sqrt{2}}\left(|0\rangle + |1\rangle + |0\rangle - |1\rangle\right)\right) \\
               &= \frac{1}{2}\left(|0\rangle + |1\rangle + |0\rangle - |1\rangle\right) \\
               &= \frac{1}{2}\left(|0\rangle + |0\rangle\right) \\
               &= |0\rangle
\end{align*}

\begin{align*}
    H|-\rangle &= H\left(\frac{1}{\sqrt{2}}\left(|0\rangle - |1\rangle\right)\right) \\
               &= \frac{1}{\sqrt{2}}\left(H|0\rangle - H|1\rangle\right) \\
               &= \frac{1}{\sqrt{2}}\left(\frac{1}{\sqrt{2}}\left(|0\rangle + |1\rangle\right) - H|1\rangle\right) \\
               &= \frac{1}{\sqrt{2}}\left(\frac{1}{\sqrt{2}}\left(|0\rangle + |1\rangle\right) - \frac{1}{\sqrt{2}}\left(|0\rangle - |1\rangle\right)\right) \\
               &= \frac{1}{\sqrt{2}}\left(\frac{1}{\sqrt{2}}\left(|0\rangle + |1\rangle - |0\rangle + |1\rangle\right)\right) \\
               &= \frac{1}{2}\left(|0\rangle + |1\rangle - |0\rangle + |1\rangle\right) \\
               &= \frac{1}{2}\left(|1\rangle + |1\rangle\right) \\
               &= |1\rangle
\end{align*}