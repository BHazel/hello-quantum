# Hello, Quantum!

Hello, Quantum! is a collection of code samples, with backing scientific and mathematical explanations, of quantum computing concepts and applications all tied together with a modern responsive web site.

I started developing Hello, Quantum! as an exercise of building my own knowledge and skills in quantum computing and wanted to share it with the world!

# Technologies

* Python
* .NET
* Material for MkDocs
* Numerous Quantum Computing Platforms
    * Please see the [Supported Platforms](docs/supported-platforms.md) page for details.

# Getting Started

Instructions for working with the quantum computing samples is available on the [Getting Started](docs/getting-started.md) page.

It is recommended to use a Python virtual environment for web site development.

```bash
pip install mkdocs-material
mkdocs serve
```

A Makefile wraps the MkDocs server and build functionality.

Command | Description
--- | ---
`make start` | Start the MkDocs server.
`make build` | Build the site into a `dist` directory.
`make clean` | Delete a built site.