echo "*** Hello, Quantum! - .NET Environment Configuration ***"

# Microsoft QDK
dotnet new -i Microsoft.Quantum.ProjectTemplates

# Jupyter Q# Kernel
dotnet tool install -g microsoft.quantum.iqsharp
dotnet iqsharp install