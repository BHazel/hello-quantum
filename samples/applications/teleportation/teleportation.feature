Feature: Teleportation
    Teleport a quantum state from one qubit to another.

    Background:
        Given I have 3 qubits in the |0> state
        And I apply gate(s) <gates> to the qubit to create the state <state> to teleport
        And I apply the Hadamard gate to qubit Alice
        And I apply the Controlled NOT gate to qubit Bob using qubit Alice as the control
        And I apply the Controlled NOT gate to the qubit Alice using the state to teleport qubit as the control
        And I apply the Hadamard gate to the state to teleport qubit

    Scenario Outline: Measurement is deferred
        And I apply the Controlled NOT gate to the qubit Bob using qubit Alice as the control
        And I apply the Controlled Z gate to the qubit Bob using the state to teleport qubit as the control
        When I measure the qubit Bob
        Then I have a <zero>% probability of a result of 0
        And I have a <one>% probability of a result of 1
        Examples:
            | gates         | state             | zero | one |
            | I             | 0                 | 100  | 0   |
            | X             | 1                 | 0    | 100 |
            | H             | 1:1 Superposition | 50   | 50  |
            | H, T, H, T, H | 3:1 Superposition | 75   | 25  |
        
    Scenario Outline: Measurement is not deferred
        And I measure the state to teleport qubit
        And I measure qubit Alice