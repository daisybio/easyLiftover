from easyliftover import liftover_path, liftover_url

def __test__(assembly1: str, assembly2: str, path_assembly1: str, path_assembly2: str):
    content_assembly1 = open(path_assembly1).read()
    content_assembly2 = open(path_assembly2).read()
    
    assert liftover_path(assembly1, assembly2, path_assembly1) == content_assembly2
    assert liftover_path(assembly2, assembly1, path_assembly2) == content_assembly1

def test_bed():
    __test__('hg19', 'hg38', 'test/data/hg19.bed', 'test/data/hg38.bed')
    
def test_gff():
    __test__('hg19', 'hg38', 'test/data/hg19.gff', 'test/data/hg38.gff')
    
def test_wig():
    __test__('hg19', 'hg38', 'test/data/hg19.wig', 'test/data/hg38.wig')
    
def test_url_lifting():
    result = liftover_url('hg19', 'hg38', 'https://github.com/biomedbigdata/easyLiftover/raw/main/test/data/hg19.bed')
    assert result == liftover_path('hg19', 'hg38', 'test/data/hg19.bed')