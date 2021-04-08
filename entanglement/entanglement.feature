Feature: Two Entangled Qubits
    Entangle two qubits and measure them.

    Scenario: Entangle two qubits and measure them.
        Given I have a control qubit in the |0> state
        And I have a target qubit in the |0> state
        And I apply the Hadamard gate to the control qubit
        And I apply the Controlled NOT gate to the target qubit using the control qubit
        When I measure the control qubit
        And I measure the target qubit
        Then I have a 50% probability of a result of 00
        And I have a 50% probability of a result of 11
        And I have a 0% probability of a result of 01
        And I have a 0% probability of a result of 10