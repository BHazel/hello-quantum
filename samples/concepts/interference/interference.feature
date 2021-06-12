Feature: Quantum Interference
    Creates a superposition and applies interference to a qubit.

    Background:
        Given I have a qubit in the |0> state

    Scenario Outline:
        And I apply <gate> gate to initialise it into the <start> state
        When I apply the Hadamard gate to create a 1:1 superposition
        And I apply another Hadamard gate to apply interference
        Then I have a <zero>% probability of a result of 0
        And I have a <one>% probability of a result of 1
        Examples:
            | start | gate | zero | one |
            | |0>   | no   | 100  | 0   |
            | |1>   | X    | 0    | 100 |