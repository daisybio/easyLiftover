from .lifters import *

def __test__(clazz, assembly1: str, assembly2: str, path_assembly1: str, path_assembly2: str):
    content_assembly1 = open(path_assembly1).read()
    content_assembly2 = open(path_assembly2).read()
    
    lifter = clazz(assembly1, assembly2)
    reversed_lifter = clazz(assembly2, assembly1)

    assert lifter.lift(content_assembly1) == content_assembly2
    assert reversed_lifter.lift(content_assembly2) == content_assembly1

def test_bed():
    __test__(BedLifter, 'hg19', 'hg38', 'test_data/hg19.bed', 'test_data/hg38.bed')
    
def test_gff():
    __test__(GffLifter, 'hg19', 'hg38', 'test_data/hg19.gff', 'test_data/hg38.gff')
    
def test_wig():
    __test__(WigLifter, 'hg19', 'hg38', 'test_data/hg19.wig', 'test_data/hg38.wig')
    