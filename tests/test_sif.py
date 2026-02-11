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
    # All the toSIF settings are to replicate PathwayCommons SIF generation as per the `toSIF` doccomment.
    toSIF(input_pathway, actual, chemDb=['chebi'], seqDb=['hgnc'], denylist=denylist, exclude=['NEIGHBOR_OF'])
    # We don't use filecmp as the downloaded files come with a BOM. We have to decode them first :/
    assert Path(artifacts_directory / 'Wnt_signaling_pathway.sif').read_text('utf-8-sig') == actual.read_text()

    # The extended variant
    actual = output_directory / 'Wnt_signaling_pathway_extended.sif'
    toSIF(input_pathway, actual, chemDb=['chebi'], seqDb=['hgnc'], denylist=denylist, exclude=['NEIGHBOR_OF'], extended=True)
    assert Path(artifacts_directory / 'Wnt_signaling_pathway_extended.sif').read_text('utf-8-sig') == actual.read_text()
