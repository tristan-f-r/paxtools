# PAXTools

[![Version](https://img.shields.io/pypi/v/paxtools.svg)](https://pypi.python.org/pypi/paxtools/)

Python wrapper for Paxtools. This requires Java to run, as this is a pip wrapper for a Java executable jar.

_This currently is only a CLI wrapper. This only contains a python utility to convert BioPAX tools to SIF._
_This satisfies my needs, though I may extend this in the future, and for some time I also plan to review and accept incoming PRs._
_If this turns out to be a false claim, feel free to email me and I'll gladly move the package name to the motivated individual!_

## CLI

Running this package directly opens the `paxtools` jar, which requires Java.
JVM arguments can be passed in with the universal environment variable `JDK_JAVA_OPTIONS`.

## Versioning

We care very little about breaking API changes in the actual API, since these largely are reflective
of Paxtools changes. Instead, the version is `<paxtools-version>-<incremented-number>`.

## Development

After cloning this repository, run:

```sh
git submodule update --init --recursive
```

which will clone the Paxtools repository under `paxtools/paxtools`.
Install [maven](https://maven.apache.org/), then run `mvn install` under `paxtools/paxtools`, which will build
the desired (and shadowed!) `paxtools/paxtools/paxtools-console/target/paxtools.jar`.

The python code under `paxtools` (`cli.py`) provides a small installation-invariant wrapper
for this tool which can be installed using `pip`.
