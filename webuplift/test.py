from django.test import TestCase
from webuplift.views.lifters import *

class HumanBedTestCase(TestCase):
    def test_bed(self):
        hg19 = open('test_data/hg19.bed').read()
        hg38 = open('test_data/hg38.bed').read()
        
        lifter = BedLifter('hg19', 'hg38')
        reversed_lifter = BedLifter('hg38', 'hg19')
        
        self.assertEquals(lifter.lift(hg19), hg38)
        self.assertEquals(reversed_lifter.lift(hg38), hg19)
        
    def test_gff(self):
        hg19 = open('test_data/hg19.gff').read()
        hg38 = open('test_data/hg38.gff').read()
        
        lifter = GffLifter('hg19', 'hg38')
        reversed_lifter = GffLifter('hg38', 'hg19')
        
        self.assertEquals(lifter.lift(hg19), hg38)
        self.assertEquals(reversed_lifter.lift(hg38), hg19)
