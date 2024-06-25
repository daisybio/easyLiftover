from easyliftover.types import get_file_types


def test_get_file_types():
    types = get_file_types()

    expected = ["bed", "gff"]

    assert all([t in types for t in expected])
