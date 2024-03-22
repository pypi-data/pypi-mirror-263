FROM ubuntu:22.04

# Install OPA
RUN apt-get update && \
    apt-get install -y wget && \
    wget https://openpolicyagent.org/downloads/latest/opa_linux_amd64 && \
    mv opa_linux_amd64 /usr/local/bin/opa && \
    chmod 755 /usr/local/bin/opa

# Set up the work directory
WORKDIR /app

# Create a directory for policies (this will be overwritten by mounted volume)
RUN mkdir /app/policies

# Expose OPA's default port
EXPOSE 8181

# Command to keep the container running without exiting
CMD ["tail", "-f", "/dev/null"]