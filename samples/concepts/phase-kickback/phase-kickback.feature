Feature: Phase Kickback
    Apply a controlled-NOT gate to two qubits in the |+> and |->
    superposition states to cause phase kickback.

    Scenario Outline:
        Given I have a control qubit in the |0> state
        And I have a target qubit in the |1> state
        And I apply the Hadamard gate to the control qubit to set it in the |+> state
        And I apply the X and Hadamard gates to the target qubit to set it in the |-> state
        And I apply a controlled-NOT gate using the control qubit as control and target qubit as the target
        When I measure the qubits in the Hadamard (X) basis
        Then I have a <percentage>% probability of a result of <result>

        Examples:
            | result | percentage |
            | ++     | 0          |
            | +-     | 0          |
            | -+     | 0          |
            | --     | 100        |