namespace BWHazel.HelloQuantum.Applications.Teleportation {

    open Microsoft.Quantum.Arrays;
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Intrinsic;

    /// # Summary
    /// Program entry point.
    @EntryPoint()
    operation Main () : Unit {
        Message("*** Hello, Quantum! - Teleportation (QDK) ***");

        let repeatCount = 1000;

        // Teleport a state of 0.
        TeleportState(repeatCount, [I], "0");

        // Teleport a state of 1.
        TeleportState(repeatCount, [X], "1");

        // Teleport a state of a 1:1 superposition.
        TeleportState(repeatCount, [H], "1:1 Superposition");

        // Teleport a state of a 3:1 superposition.
        TeleportState(repeatCount, [H, T, H, T, H], "3:1 Superposition");
    }

    operation TeleportState (repeatCount : Int, operations : (Qubit => Unit is Adj+Ctl)[], description: String) : Unit {
        mutable onesCount = 0;

        for i in 1..repeatCount {
            // Allocate qubit.
            use stateToTeleport = Qubit();

            // Prepare qubit into state to teleport.
            for op in operations {
                op(stateToTeleport);
            }

            let teleportResult = Teleport(stateToTeleport, false);
            set onesCount += teleportResult;
            Reset(stateToTeleport);
        }

        // Print results.
        Message($"Counts for {repeatCount} repeats for teleported state {description}:");
        Message($"\t0: {repeatCount - onesCount}");
        Message($"\t1: {onesCount}");
    }

    /// # Summary
    /// Teleport the specified qubit.
    ///
    /// # Input
    /// ## stateToTeleport
    /// The qubit in the state to teleport.
    ///
    /// ## deferMeasurement
    /// A value indicating if measurement should be deferred to the end of the circuit.
    ///
    /// # Output
    /// The result of measuring the target qubit.
    operation Teleport (stateToTeleport : Qubit, deferMeasurement : Bool) : Int {
        use (alice, bob) = (Qubit(), Qubit());

        // Entangle Alice's and Bob's qubits.
        H(alice);
        CNOT(alice, bob);

        // Entangle qubit with the state to teleport with the
        // existing entangled state of Alice's and Bob's qubits.
        CNOT(stateToTeleport, alice);
        
        H(stateToTeleport);

        if deferMeasurement == true {
            Controlled X([alice], bob);
            Controlled Z([stateToTeleport], bob);
        } else {
            let stateToTeleportResult = M(stateToTeleport);
            let aliceResult = M(alice);

            // If Alice's qubit is measured as 1, apply the X gate to Bob's qubit.
            if aliceResult == One {
                X(bob);
            }

            // If the qubit to teleport is measured as 1, apply the Z gate to Bob's qubit.
            if (stateToTeleportResult == One) {
                Z(bob);
            }
        }

        let bobResult = M(bob);
        ResetAll([alice, bob]);

        return ResultArrayAsInt([bobResult]);
    }
}

