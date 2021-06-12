namespace BWHazel.HelloQuantum.Concepts.Interference {

    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;

    /// # Summary
    /// Program entry point.
    @EntryPoint()
    operation Main () : Unit {
        Message("*** Hello, Quantum! - Interference (QDK) ***");

        let repeatCount = 1000;
        
        // Cause interference on a qubit starting in the 0 state.
        let startingStateZeroCount = Interference(repeatCount, Zero);

        // Cause interference on a qubit starting in the 1 state.
        let startingStateOneCount = Interference(repeatCount, One);

        // Print results.
        Message($"Counts for {repeatCount} repeats with starting state 0:");
        Message($"\t0: {startingStateZeroCount}");
        Message($"\t1: {repeatCount - startingStateZeroCount}");
        Message($"Counts for {repeatCount} repeats with starting state 1:");
        Message($"\t0: {repeatCount - startingStateOneCount}");
        Message($"\t1: {startingStateOneCount}");
    }

    /// # Summary
    /// Creates a superposition and applies interference on a qubit in a
    /// specified state a specified number of times.
    ///
    /// # Input
    /// ## repeatCount
    /// The number of times to repeat the quantum circuit.
    /// ## startingState
    /// The state to set the qubit to prior to running the quantum circuit.
    ///
    /// # Output
    /// The count where the measurement result is the starting state.
    operation Interference (repeatCount : Int, startingState : Result) : Int {
        mutable startingStateCount = 0;
        
        // Repeat quantum circuit a specified number of times.
        for i in 1..repeatCount {
            // Allocate qubit.
            use qubit = Qubit();

            // Set qubit to desired starting state.
            // If the starting state should be 1, apply the X gate.
            if (M(qubit) != startingState) {
                X(qubit);
            }

            // Apply Hadamard gate to create a superposition.
            H(qubit);

            // Apply Hadamard gate to cause interference to restore qubit to its starting state.
            H(qubit);

            // Measure qubit and update count if result is the starting state.
            let qubitMeasurement = M(qubit);
            if qubitMeasurement == startingState {
                set startingStateCount += 1;
            }

            // Reset qubit to 0 state.
            Reset(qubit);
        }

        return startingStateCount;
    }
}