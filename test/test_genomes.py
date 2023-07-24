from easyliftover import get_genomes

def test_targets():
    assert "hg38" in get_genomes()