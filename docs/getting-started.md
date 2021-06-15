# Getting Started

All the code samples and this site are hosted in a public [GitHub repository](https://github.com/bhazel/hello-quantum).  I encourage you to download it to run and experiment with the samples!

## Environment Setup

My personal recommendation is to use a **Docker image**.  A `Dockerfile` is included in the root of the repository to build an image of the repository and configure its Python and .NET dependencies including the Rigetti Forest tooling.  It also includes both [Jupyter and JupyterLab](https://jupyter.org) configured with the Python and Q# kernels.

```bash
docker image build -t x-hello-quantum .
```

Alternatively, you will need to install:

* [Python 3](https://www.python.org)
* [.NET Core 3.1](https://dotnet.microsoft.com)

You can then install the required libraries and tooling for the platforms.  I would strongly recommend using a virtual environment for the Python components.

* **Configuration Scripts:** Shell scripts to install and configure the Python and .NET libraries are included in the `tools/configuration` directory of the repository.
> **Please note:** You will need to manually install the Rigetti Forest SDK tools as outlined on the [Supported Platforms](supported-platforms.html) page.
* **Manual Installation:** Basic installation instructions are included on the [Supported Platforms](supported-platforms.html) page.  Links to the platforms for additional information and instructions are included.