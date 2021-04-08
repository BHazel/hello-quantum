Feature: Single Qubit Superposition
    Create a superposition between the |0> and |1> states
    for a single qubit and measure it.

    Scenario: Create and measure a superposition
        Given I have a qubit in the |0> state
        And I apply the Hadamard gate to the qubit
        When I measure the qubit
        Then I have a 50% probability of a result of 0
        And I have a 50% probability of a result of 1