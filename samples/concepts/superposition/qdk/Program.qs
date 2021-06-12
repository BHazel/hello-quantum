namespace BWHazel.HelloQuantum.Concepts.Superposition {

    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;

    /// # Summary
    /// Program entry point.
    @EntryPoint()
    operation Main () : Unit {
        Message("*** Hello, Quantum! - Superposition (QDK) ***");

        let repeatCount = 1000;
        mutable onesCount = 0;
        
        // Repeat quantum circuit a specified number of times.
        for i in 0..repeatCount {
            // Allocate qubit.
            // Apply Hadamard gate to create a superposition.
            use qubit = Qubit();
            H(qubit);

            // Measure qubit and update count if result is 1.
            let qubitMeasurement = M(qubit);
            if qubitMeasurement == One {
                set onesCount += 1;
            }

            // Reset qubit to 0 state.
            Reset(qubit);
        }

        // Print results.
        Message($"Counts for {repeatCount} repeats:");
        Message($"\t0: {repeatCount - onesCount}");
        Message($"\t1: {onesCount}");
    }
}

