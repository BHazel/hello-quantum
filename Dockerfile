FROM python
LABEL maintainer="Benedict W. Hazel"
SHELL ["/bin/bash", "-c"]

ARG dotnet_version="3.1.416"
ARG forest_sdk_version="2.23.0"

# Install .NET Core
RUN wget -O dotnet-install.sh https://dot.net/v1/dotnet-install.sh && \
    chmod 777 dotnet-install.sh && \
    ./dotnet-install.sh --version ${dotnet_version}
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