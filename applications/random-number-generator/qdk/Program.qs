namespace BWHazel.HelloQuantum.RandomNumberGenerator {

    open Microsoft.Quantum.Arrays;
    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;

    /// # Summary
    /// Program entry point.
    @EntryPoint()
    operation Main () : Unit {
        Message("*** Hello, Quantum! - Random Number Generator (QDK) ***");
        
        let repeatCount = 10;
        mutable randomNumbers = EmptyArray<Int>();

        // Repeat random number generation a specified number of times.
        for i in 1..repeatCount {
            let randomNumber = GenerateRandomNumber();
            set randomNumbers += [randomNumber];
        }

        // Print random numbers.
        Message($"Random numbers from {repeatCount} repeats:");
        for randomNumber in randomNumbers {
            Message($"\t{randomNumber}");
        }
    }

    /// # Summary
    /// Generates a random number between 0-15.
    ///
    /// # Output
    /// A random number between 0-15.
    operation GenerateRandomNumber () : Int {
        // Allocate 4 qubits.
        // Apply Hadamard gate to all qubits.
        use qubits = Qubit[4];
        for qubit in qubits {
            H(qubit);
        }

        // Measure all qubits.
        // Convert measurement results as binary digits into integer.
        let qubitMeasurements = MultiM(qubits);
        let numberFromMeasurement = ResultArrayAsInt(qubitMeasurements);

        // Reset qubits to 0 state.
        ResetAll(qubits);

        // Return random number.
        return numberFromMeasurement;
    }
}

