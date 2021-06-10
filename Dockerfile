FROM python
LABEL maintainer="Benedict W. Hazel"
SHELL ["/bin/bash", "-c"]

ARG forest_sdk_version="2.23.0"

# Install .NET Core
RUN bash -c "$(curl -fsSL https://dot.net/v1/dotnet-install.sh)"
ENV DOTNET_ROOT "/root/.dotnet"
ENV PATH "$DOTNET_ROOT:$DOTNET_ROOT/tools:$PATH"

# Install Rigetti Forest SDK & QVM
WORKDIR /tmp
RUN wget -O forest-sdk.tar.bz2 http://downloads.rigetti.com/qcs-sdk/forest-sdk-${forest_sdk_version}-linux-deb.tar.bz2 && \
    tar -xf forest-sdk.tar.bz2 && \
    apt-get update && \
    yes | ./forest-sdk-${forest_sdk_version}-linux-deb/forest-sdk-${forest_sdk_version}-linux-deb.run

# Configure Python & .NET Environments
WORKDIR /hello-quantum
COPY . .
RUN bash tools/configuration/python_environment.sh && \
    bash tools/configuration/dotnet_environment.sh

# Configure JupyterLab
CMD jupyter-lab --allow-root --ip "*"
EXPOSE 8888