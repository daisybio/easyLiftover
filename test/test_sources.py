from easyliftover.sources import get_sources


def test_get_file_sources():
    sources = get_sources()

    assert len(sources) > 0
