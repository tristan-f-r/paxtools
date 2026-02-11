# Artifacts

Test artifacts. The `Wnt_*` family of files is from the _PANTHER_ Wnt signaling pathway: https://apps.pathwaycommons.org/pathways?uri=https%3A%2F%2Fidentifiers.org%2Fpanther.pathway%3AP00057,
under SIF, Extended SIF, and BioPAX for `_extended.sif`, `.sif`, and `.xml` respectively.

`pc2-14-denylist.txt` is from https://download.baderlab.org/PathwayCommons/PC2/v14/blacklist.txt, which is the list of small molecules that the server converter denies. You can specify it with `-Dpaxtools.pattern.blacklist=<path>` under your JVM options (more information is available in the Paxtools README), or use the provided Python API.

If you want to generate the denylist yourself, the Java code is available at [BlacklistGenerator3.java](https://github.com/BioPAX/Paxtools/blob/aaceda2c83f744645859008f4b37a54a840760a9/pattern/src/main/java/org/biopax/paxtools/pattern/miner/BlacklistGenerator3.java), and I would gladly welcome a PR which wraps the `paxtools blacklist <input> <output>` command.
