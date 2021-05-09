import argparse
from pytket.backends import Backend
from pytket.extensions.qiskit import AerBackend

backends = {
    'qiskit': AerBackend()
}

def get_backend(backend: str) -> Backend:
    """Gets the tket backend for the specified platform.

    Args:
        backend (str): The backend platform.

    Returns:
        pytket.backends.Backend: The tket backend for the specified platform.
    """
    tket_backend = None
    if backend in backends:
        tket_backend = backends[backend]

    return tket_backend


def get_tket_backend() -> Backend:
    """Gets the tket backend specified in command-line arguments.

    Asserts that a backend must be initialised prior to returning to the calling function.

    Returns:
        pytket.backends.Backend: The tket backend for the specified platform.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--backend', help='Specified platform backend.')
    args = parser.parse_args()

    backend = get_backend(args.backend)

    assert (backend is not None), 'Backend not recognised'
    return backend