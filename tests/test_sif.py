import filecmp
from pathlib import Path
from paxtools.sif import toSIF

current_directory = Path(__file__).parent.resolve()
artifacts_directory = current_directory / 'artifacts'
output_directory = current_directory / 'output'

def test_sif():
    output_directory.mkdir(exist_ok=True)
    input_pathway = artifacts_directory / 'Wnt_signaling_pathway.xml'
    denylist = artifacts_directory / 'pc2-14-denylist.txt'
    
    actual = output_directory / 'Wnt_signaling_pathway.sif'
    toSIF(input_pathway, actual, useNameIfNoId=True, chemDb=['chebi'], seqDb=['hgnc'], denylist=denylist)
    assert filecmp.cmp(artifacts_directory / 'Wnt_signaling_pathway.sif', actual, shallow=True)

    # The extended variant
    actual = output_directory / 'Wnt_signaling_pathway_extended.sif'
    toSIF(input_pathway, actual, useNameIfNoId=True, chemDb=['chebi'], seqDb=['hgnc'], denylist=denylist)
    assert filecmp.cmp(artifacts_directory / 'Wnt_signaling_pathway_extended.sif', actual, shallow=True)
