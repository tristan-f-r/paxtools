from pathlib import Path
from paxtools.sif import toSIF

current_directory = Path(__file__).parent.resolve()
artifacts_directory = current_directory / 'artifacts'
output_directory = current_directory / 'output'

def test_sif():
    output_directory.mkdir(exist_ok=True)
    toSIF(
        artifacts_directory / 'Wnt_signaling_pathway.xml',
        output_directory / 'Wnt_signaling_pathway.sif'
    )

    toSIF(
        artifacts_directory / 'Wnt_signaling_pathway.xml',
        output_directory / 'Wnt_signaling_pathway_extended.sif',
        extended=True
    )
