namespace BWHazel.HelloQuantum.Concepts.Entanglement {

    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic; 

    /// # Summary
    /// Program entry point.
    @EntryPoint()
    operation Main () : Unit {
        Message("*** Hello, Quantum! - Entanglement (QDK) ***");

        let repeatCount = 1000;
        mutable zeroZeroCount = 0;
        mutable zeroOneCount = 0;
        mutable oneZeroCount = 0;
        mutable oneOneCount = 0;

        // Repeat quantum circuit a specified number of times.
        for i in 1..repeatCount {
            // Allocate qubits.
            // Apply Hadamard gate to the control qubit.
            // Apply Controlled NOT gate to the target qubit using the control qubit.
            use (controlQubit, targetQubit) = (Qubit(), Qubit());
            H(controlQubit);
            CNOT(controlQubit, targetQubit);

            // Measure qubits.
            let controlQubitMeasurement = M(controlQubit);
            let targetQubitMeasurement = M(targetQubit);

            // Set counts based on qubit measurement results.
            set zeroZeroCount += (controlQubitMeasurement == Zero and targetQubitMeasurement == Zero) ? 1 | 0;
            set zeroOneCount += (controlQubitMeasurement == Zero and targetQubitMeasurement == One) ? 1 | 0;
            set oneZeroCount += (controlQubitMeasurement == One and targetQubitMeasurement == Zero) ? 1 | 0;
            set oneOneCount += (controlQubitMeasurement == One and targetQubitMeasurement == One) ? 1 | 0;

            // Reset qubits to 0 state.
            ResetAll([controlQubit, targetQubit]);
        }

        // Print results.
        Message($"Counts for {repeatCount} repeats:");
        Message($"\t00: {zeroZeroCount}");
        Message($"\t01: {zeroOneCount}");
        Message($"\t10: {oneZeroCount}");
        Message($"\t11: {oneOneCount}");
    }
}

