from easyliftover.lifters.pyliftover.pyliftover.chainfile import open_liftover_chain_file

def test_chain_file():
    res = open_liftover_chain_file('hg19', 'hg38', search_dir=None, cache_dir=None, use_web=True, write_cache=True)

    assert res is not None