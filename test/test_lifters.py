from easyliftover import *

def __test__(clazz, assembly1: str, assembly2: str, path_assembly1: str, path_assembly2: str):
    content_assembly1 = open(path_assembly1).read()
    content_assembly2 = open(path_assembly2).read()
    
    lifter: AbstractLifter = clazz(assembly1, assembly2)
    reversed_lifter: AbstractLifter = clazz(assembly2, assembly1)

    assert lifter.lift_path(path_assembly1) == content_assembly2
    assert reversed_lifter.lift_path(path_assembly2) == content_assembly1

def test_bed():
    __test__(BedLifter, 'hg19', 'hg38', 'test/data/hg19.bed', 'test/data/hg38.bed')
    
def test_gff():
    __test__(GffLifter, 'hg19', 'hg38', 'test/data/hg19.gff', 'test/data/hg38.gff')
    
def test_wig():
    __test__(WigLifter, 'hg19', 'hg38', 'test/data/hg19.wig', 'test/data/hg38.wig')
