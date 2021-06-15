# Supported Platforms

The currently supported platforms in Hello, Quantum! are outlined in the table belwo.  Each code sample in the source code contains directories for each supported platform, also outlined in the table.

Platform | Technology | Sample Directories | Installation
--- | --- | --- | ---
[CQC tket](https://cqcl.github.io/pytket/build/html) | Python 3 | `tket` | `pip install pytket` <sup>1</sup>
[Google Cirq](https://quantumai.google/cirq) | Python 3 | `cirq` | `pip install cirq`
[IBM Qiskit](https://qiskit.org) | Python 3 | `qiskit` | `pip install qiskit`
[Microsoft QDK](https://docs.microsoft.com/en-gb/azure/quantum/) | .NET Core 3.1 | `qdk` | `dotnet new -i Microsoft.Quantum.ProjectTemplates`
[Rigetti Forest](https://pyquil-docs.rigetti.com/en/stable) | Python 3 | `forest` | `pip install pyquil` <sup>2</sup>

> <sup>1</sup> You will need to install tket backends separately as outlined in the documentation.

> <sup>2</sup> You will need to install the Rigetti Forest SDK tooling, which includes `quilc` and `qvm`, from the Rigetti Computing site.