namespace BWHazel.HelloQuantum.Concepts.MeasurementBases {

    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;

    /// # Summary
    /// Program entry point.
    @EntryPoint()
    operation Main () : Unit {
        Message("*** Hello, Quantum! - Measurement Bases (QDK) ***");

        let repeatCount = 1000;

        // Create and measure a superposition in the Computational Basis (Z-Basis).
        let computationalBasisOnesCount = Superposition(repeatCount, PauliZ);
        
        // Create and measure a superposition in the Hadamard Basis (X-Basis).
        let hadamardBasisOnesCount = Superposition(repeatCount, PauliX);

        // Print results.
        Message($"Counts for {repeatCount} repeats in Computational Basis:");
        Message($"\t0: {repeatCount - computationalBasisOnesCount}");
        Message($"\t1: {computationalBasisOnesCount}");
        Message($"Counts for {repeatCount} repeats in Hadamard Basis:");
        Message($"\t0: {repeatCount - hadamardBasisOnesCount}");
        Message($"\t1: {hadamardBasisOnesCount}");
    }

    /// # Summary
    /// Creates a superposition and measures it using a specified basis a
    /// specified number of times.
    ///
    /// # Input
    /// ## repeatCount
    /// The number of times to repeat the quantum circuit.
    /// ## measurementBasis
    /// The basis to perform the measurement with.
    ///
    /// # Output
    /// The count where the measurement result is 1.
    operation Superposition(repeatCount : Int, measurementBasis : Pauli) : Int {
        mutable onesCount = 0;

        // Repeat quantum circuit a specified number of times.
        for i in 1..repeatCount {
            // Allocate qubit.
            use qubit = Qubit();

            // Measure qubit using the specified basis and update count if result is 1.
            let qubitMeasurement = Measure([measurementBasis], [qubit]);
            set onesCount += qubitMeasurement == One ? 1 | 0;
        }

        return onesCount;
    }
}

