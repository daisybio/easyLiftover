from easyliftover.types import get_file_types

def test_get_file_types():
    types = get_file_types()
    
    assert len(types) > 0