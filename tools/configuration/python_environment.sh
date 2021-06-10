echo "*** Hello, Quantum! - Python Environment Configuration ***"

# Microsoft QDK & Azure Quantum
pip install \
    qsharp \
    azure-quantum

# IBM Qiskit
pip install \
    qiskit \
    git+https://github.com/qiskit-community/qiskit-textbook.git#subdirectory=qiskit-textbook-src \
    pylatexenc

# Rigetti Forest
pip install pyquil

# Google Cirq
pip install cirq

# CQC tket
pip install \
    pytket \
    pytket-qiskit

# Additional Tools
pip install jupyterlab