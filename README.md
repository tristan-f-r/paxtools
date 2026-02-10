# PAXTools

Python wrapper for PAXTools. This requires Java to run, as this is a pip wrapper for a Java executable jar.

_This currently is only a CLI wrapper. This will be extended to contain some basic utilities around PAXTools's core CLI._
_This satisfies my needs, though I may extend this in the future. If this turns out to be a false claim,_
_feel free to email me and I'll gladly move the package name to the motivated individual!_

## Development

After cloning this repository, run:

```sh
git submodule update --init --recursive
```

which will clone the paxtools repository under `paxtools/paxtools`.
Install [maven](https://maven.apache.org/), then run `mvn install` under `paxtools/paxtools`, which will build
the desired (and shadowed!) `paxtools/paxtools/paxtools-console/target/paxtools.jar`.

The python code under `paxtools` (`cli.py`) provides a small installation-invariant wrapper
for this tool which can be installed using `pip`.
