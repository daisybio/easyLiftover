from .abstract import AbstractLifter
import tempfile
import requests

class BigWigLifter(AbstractLifter):
    def lift_path(self, path: str) -> str:
        """Lifts a path."""
        import pyBigWig
        bw = pyBigWig.open(path)
        
        return self.lift_bw(bw)
    
    def lift_url(self, url: str) -> str:
        """Lifts a URL."""
        tempfile_path = tempfile.NamedTemporaryFile().name
        
        with open(tempfile_path, "wb") as f:
            f.write(requests.get(url).content)
            
        return self.lift_path(tempfile_path)

    def lift_bw(self, bw) -> str:
        wig = ""
                
        for chromosome in bw.chroms():
            chromosome_with_prefix = f"chr{chromosome}" if not chromosome.startswith("chr") else chromosome
                
            prev_span: int = -1
            for start, end, value in bw.intervals(chromosome):
                rounded_value = round(value, 2)
                
                lifted = self.convert_region(chromosome_with_prefix, start, end)
                
                if lifted is not None:
                    lifted_chromosome, lifted_start, lifted_end = lifted
                    span = lifted_end - lifted_start
                    
                    if span != prev_span:
                        wig += f"variableStep chrom={lifted_chromosome} span={span}\n"
                        prev_span = span
                    
                    wig += f"{lifted_start}\t{rounded_value}\n"
        
        return wig