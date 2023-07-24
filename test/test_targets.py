from easyliftover import get_targets

def test_targets():
    assert "Hg38" in get_targets("hg19")