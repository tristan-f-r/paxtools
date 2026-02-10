# PAXTools

Python wrapper for Paxtools. This requires Java to run, as this is a pip wrapper for a Java executable jar.

_This currently is only a CLI wrapper. This only contains a python utility to convert BioPAX tools to SIF._
_This satisfies my needs, though I may extend this in the future. If this turns out to be a false claim,_
_feel free to email me and I'll gladly move the package name to the motivated individual!_

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
