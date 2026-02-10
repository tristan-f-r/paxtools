"""
Converts BioPAX files to SIF files
"""

import os
import subprocess
from paxtools.cli import run

class SifConversionFailure(Exception):
    pass


def optional(value: str, show: bool) -> list[str]:
    return [value] if show else []

def toSIF(
        biopax: str | os.PathLike, output_sif: str | os.PathLike,
        include: list[str] = [], exclude: list[str] = [],
        extended: bool = False,
        seqDb: list[str] = [], chemDb: list[str] = [],
        mergeInteractions: bool = True, useNameIfNoId: bool = False,
        properyAccessors: list[str] = [],
        andSif: bool = False):
    """
    Equivalent to `paxtools toSIF ...`. This documentation is paraphrased from the main paxtools CLI.
    @param biopax: The input BioPAX file
    @param output: The output file for the SIF-like text format
    @param include: List of relationship types to include
        (mind using underscore instead of minus sign in the SIF type names; the default is to use all types).
    @param exclude: List of relationship types to exclude
        (mind using underscore instead of minus sign in the SIF type names; the default is to use all types).
    @param mergeInteractions: Merges equivalent interactions
    @param seqDb: standard sequence/gene/chemical ID types to match xref.db values
    @param chemDb: standard sequence/gene/chemical ID types to match xref.db values
        - By default, this goes to 'hgnc' (in fact, 'HGNC Symbol') for bio-polymers
    @param useNameIfNoId: Uses the name if no ID is set for ChEBI references.
    @param properyAccessors: specifies 4th, 5th etc. custom output columns;
        use pre-defined column names (accessors): 
            MEDIATOR,
            PUBMED,
            PMC,
            COMMENTS,
            PATHWAY,
            PATHWAY_URI,
            RESOURCE,
            SOURCE_LOC,
            TARGET_LOC
        or custom biopax property path accessors (XPath-like expressions to apply to each mediator entity; 
        see https://github.com/BioPAX/Paxtools/wiki/PatternBinaryInteractionFramework)
    @param andSif: Also creates a `.sif` file adjacent to output. The author finds this parameter ridiculous, and recommends just calling this method twice.
    """
    process = run([
        'toSIF', str(biopax), str(output_sif),
        *optional(f'include={",".join(include)}', len(include) != 0),
        *optional(f'exclude={",".join(exclude)}', len(exclude) != 0),
        *optional(f'seqDb={",".join(seqDb)}', len(seqDb) != 0),
        *optional(f'chemDb={",".join(chemDb)}', len(chemDb) != 0),
        *optional("-extended", extended),
        *optional("-andSif", andSif),
        *optional("-dontMergeInteractions", not mergeInteractions),
        *optional("--useNameIfNoId", useNameIfNoId),
        *properyAccessors
    ], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

    if process.returncode != 0:
        raise SifConversionFailure(f"Conversion errored with code {process.returncode}: {process.stderr.decode('utf-8')}")
