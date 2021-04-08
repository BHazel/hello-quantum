Feature: Measurement with Different Bases
    Create a superposition and measure it using different bases.

    Background:
        Given I have a qubit in the |0> state
        And I apply the Hadamard gate to the qubit
    
    Scenario Outline: Measure in a specified basis
        When I measure the qubit in the <basis> basis
        Then I have a <zero>% probability of a result of 0
        And I have a <one>% probability of a result of 1
        Examples:
            | basis             | zero | one |
            | Computational (Z) | 50   | 50  |
            | Hadamard      (X) | 100  | 0   |
