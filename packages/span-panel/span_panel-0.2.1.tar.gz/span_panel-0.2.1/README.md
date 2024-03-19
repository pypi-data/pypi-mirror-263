# Unofficial SPAN Panel Python API and CLI

[![Latest PyPI version](https://img.shields.io/pypi/v/span-panel)](https://pypi.org/project/span-panel/) [![Supported Python](https://img.shields.io/pypi/pyversions/span-panel)](https://pypi.org/project/span-panel/) [![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![CI](https://github.com/AngellusMortis/span-panel/actions/workflows/ci.yaml/badge.svg)](https://github.com/AngellusMortis/span-panel/actions/workflows/ci.yaml) [![Documentation](https://github.com/AngellusMortis/span-panel/actions/workflows/pages/pages-build-deployment/badge.svg)](https://angellusmortis.github.io/span-panel/)

`span-panel` is an unofficial API for the [SPAN Smart Panel](https://www.span.io/panel). There is no affiliation with SPAN.

## Documentation

[Full documentation for the project](https://angellusmortis.github.io/span-panel/).

## Requirements

* A [SPAN Smart Panel](https://www.span.io/panel).
    * Latest version of library is generally only tested against the latest firmware version.
* [Python](https://www.python.org/) 3.9+
* POSIX compatible system
    * Library is only test on Linux, specifically the latest Debian version available for the official Python Docker images, but there is no reason the library should not work on any Linux distro or MacOS.

Alternatively you can use the [provided Docker container](#using-docker-container), in which case the only requirement is [Docker](https://docs.docker.com/desktop/) or another OCI compatible orchestrator (such as Kubernetes or podman).

Windows is **not supported**. If you need to use `span-panel` on Windows, use Docker Desktop and the provided docker container or [WSL](https://docs.microsoft.com/en-us/windows/wsl/install).

## Install

### From PyPi

`span-panel` is available on PyPi:

```bash
pip install span-panel
```

### From Github

```bash
pip install git+https://github.com/AngellusMortis/span-panel.git#egg=span-panel
```

### Using Docker Container

A Docker container is also provided so you do not need to install/manage Python as well. You can add the following to your `.bashrc` or similar.

```bash
function span-panel() {
    docker run --rm -it \
      -e SPAN_HOST=http://your_span_ip \
      -e SPAN_TOKEN=your_token \
      ghcr.io/angellusmortis/span-panel:latest "$@"
}
```

Some notes about the Docker version since it is running inside of a container:

* You can update at any time using the command `docker pull ghcr.io/AngellusMortis/span-panel:latest`
* The container supports `linux/amd64` and `linux/arm64` natively. This means it will also work well on MacOS or Windows using Docker Desktop.

## Quickstart

### Getting an Auth Token

Before being able to do anything, you need to get an auth token from your SPAN Panel. The `generate-token` subcommand will walk you through how.

```bash
export SPAN_HOST=http://your_span_ip

span-panel generate-token
```

### CLI

```bash
export SPAN_HOST=http://your_span_ip
export SPAN_TOKEN=your_token

span-panel --help
span-panel panel meter
span-panel circuits list-ids
```

### Python

`span-panel` itself is 100% async, so as such this library is primarily designed to be used in an async context.

The main interface for the library is the `span_panel.SpanClient`:

```python
import asyncio

from span_panel import SpanClient


client = SpanClient(host=host, token=token)

async def main():
    return await client.get_circuits()

for circuit_id, circuit in asyncio.run(main()).circuits:
    # do stuff
```
