from django.test import TestCase
from webuplift.views.uplift import __process_bed__

class HumanBedTestCase(TestCase):
    def test_works(self):
        hg19 = open('test_data/hg19.bed').read()
        hg38 = open('test_data/hg38.bed').read()
        
        self.assertEquals(__process_bed__(hg19, 'hg19', 'hg38'), hg38)
