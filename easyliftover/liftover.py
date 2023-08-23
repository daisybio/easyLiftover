from .lifters import BedLifter, GffLifter, WigLifter, AbstractLifter, BigWigLifter, BedGraphLifter

def get_lifter(fromGenome: str, toGenome: str, source: str, file_type: "str | None" = None) -> AbstractLifter:
    def get_class(c_type):
        if c_type == "bed":
            return BedLifter
        elif c_type in ["gff", "gff3", "gtf"]:
            return GffLifter
        elif c_type == "wig":
            return WigLifter
        elif c_type == "bw" or c_type == "bigwig":
            return BigWigLifter
        elif c_type == "bedgraph" or c_type == "bg":
            return BedGraphLifter
        else:
            raise Exception("Unsupported file type")
        
    def __get_type(path: str) -> str:
        return path.split(".")[-1]
        
    chosen_type = file_type if file_type is not None else __get_type(source)
        
    return get_class(chosen_type.lower())(fromGenome, toGenome)

def liftover_url(
    fromGenome: str, toGenome: str, url: str, file_type: "str | None" = None
) -> str:
    
    lifter = get_lifter(fromGenome, toGenome, url, file_type)
    
    return lifter.lift_url(url)

def liftover_path(
    fromGenome: str, toGenome: str, path: str, file_type: "str | None" = None
) -> str:
    lifter = get_lifter(fromGenome, toGenome, path, file_type)
    return lifter.lift_path(path)
