Feature: 4-Qubit Random Number Generator
    Generate a random number from 0-15 using 4 qubits in superposition.

    Scenario: Generate Random Number from 0-15
        Given I have 4 qubits in the |0> state
        And I apply the Hadamard gate to all 4 qubits
        When I measure all 4 qubits
        And I combine the results as binary digits to form an integer
        Then I have a random number between 0 and 15