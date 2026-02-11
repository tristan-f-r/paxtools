from io import StringIO
from pathlib import Path
from paxtools.sif import toSIF
import pandas
import pandas.testing

current_directory = Path(__file__).parent.resolve()
artifacts_directory = current_directory / "artifacts"
output_directory = current_directory / "output"


def test_sif():
    output_directory.mkdir(exist_ok=True)
    input_pathway = artifacts_directory / "Wnt_signaling_pathway.xml"
    denylist = artifacts_directory / "pc2-14-denylist.txt"

    actual = output_directory / "Wnt_signaling_pathway.sif"
    # All the toSIF settings are to replicate PathwayCommons SIF generation as per the `toSIF` doccomment.
    toSIF(
        input_pathway,
        actual,
        chemDb=["chebi"],
        seqDb=["hgnc"],
        denylist=denylist,
        exclude=["NEIGHBOR_OF"],
    )
    # We don't use filecmp as the downloaded files come with a BOM. We have to decode them first :/
    assert (
        Path(artifacts_directory / "Wnt_signaling_pathway.sif").read_text("utf-8-sig")
        == actual.read_text()
    )

    # The extended variant. TODO: suspicious data loss in columns outside of PARTICIPANT_A, INTERACTION_TYPE, PARTICIPANT_B?
    # For my purposes, I don't really care.
    actual = output_directory / "Wnt_signaling_pathway_extended.sif"
    toSIF(
        input_pathway,
        actual,
        chemDb=["chebi"],
        seqDb=["hgnc"],
        denylist=denylist,
        exclude=["NEIGHBOR_OF"],
        extended=True,
    )

    # TODO: also check for _expected_text_2 and _actual_text_2 later
    expected_text_1, _expected_text_2 = (
        (artifacts_directory / "Wnt_signaling_pathway_extended.sif")
        .read_text("utf-8-sig")
        .split("\n\n")
    )
    actual_text_1, _actual_text_2 = actual.read_text().split("\n\n")

    expected = pandas.read_csv(
        StringIO(expected_text_1),
        sep="\t",
        usecols=["PARTICIPANT_A", "INTERACTION_TYPE", "PARTICIPANT_B"],
    )
    actual = pandas.read_csv(
        StringIO(actual_text_1),
        sep="\t",
        usecols=["PARTICIPANT_A", "INTERACTION_TYPE", "PARTICIPANT_B"],
    )
    pandas.testing.assert_frame_equal(expected, actual)
