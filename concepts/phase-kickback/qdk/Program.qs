namespace BWHazel.HelloQuantum.Concepts.PhaseKickback {

    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;

    /// # Summary
    /// Program entry point.
    @EntryPoint()
    operation Main () : Unit {
        Message("*** Hello, Quantum! - Phase Kickback (QDK) ***");

        let repeatCount = 1000;
        mutable plusPlusCount = 0;
        mutable plusMinusCount = 0;
        mutable minusPlusCount = 0;
        mutable minusMinusCount = 0;

        // Repeat quantum circuit a specified number of times.
        for i in 1..repeatCount {
            // Allocate control and target qubits.
            use (control, target) = (Qubit(), Qubit());
            
            // Apply Hadamard gate to control qubit to create a superposition in
            // the (+)-superposition state.
            H(control);

            // Apply X gate to target qubit to set it to the 1 state.
            // Apply Hadamard gate to target qubit to create a superposition in
            // the (-)-superposition state.
            X(target);
            H(target);

            // Apply CNOT gate to target qubit using the control qubit to trigger
            // phase kickback onto the control qubit.
            CNOT(control, target);

            // Measure qubits and update counts if the results are 1.
            let controlQubitMeasurement = Measure([PauliX], [control]);
            let targetQubitMeasurement = Measure([PauliX], [target]);

            // Set counts based on qubit measurement results.
            set plusPlusCount += (controlQubitMeasurement == Zero and targetQubitMeasurement == Zero) ? 1 | 0;
            set plusMinusCount += (controlQubitMeasurement == Zero and targetQubitMeasurement == One) ? 1 | 0;
            set minusPlusCount += (controlQubitMeasurement == One and targetQubitMeasurement == Zero) ? 1 | 0;
            set minusMinusCount += (controlQubitMeasurement == One and targetQubitMeasurement == One) ? 1 | 0;

            // Reset qubits to 0 state.
            ResetAll([control, target]);
        }

        // Print results.
        Message($"Counts for {repeatCount} repeats:");
        Message($"\t++: {plusPlusCount}");
        Message($"\t+-: {plusMinusCount}");
        Message($"\t-+: {minusPlusCount}");
        Message($"\t--: {minusMinusCount}");
    }
}

