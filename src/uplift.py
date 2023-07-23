from .lifters import AbstractLifter, BedLifter, GffLifter, WigLifter

def uplift(fromGenome: str, toGenome: str, path: str, file_type: str | None = None) -> str:
    """Uplifts a genomic position from one genome build to another.

    Args:
        req: The request object.

    Returns:
        A response object with the uplifted position.
    """

    file_content = open(path, "r").read()
    file_extension = path.split(".")[-1]

    used_type = file_type if file_type is not None else file_extension

    if used_type == "bed":
        LifterClass = BedLifter
    elif used_type in ["gff", "gff3", "gtf"]:
        LifterClass = GffLifter
    elif used_type == "wig":
        LifterClass = WigLifter
    else:
        raise Exception("Unsupported file type")

    print("Initializing lifter", LifterClass, "with", fromGenome, toGenome)

    lifter = LifterClass(fromGenome, toGenome)

    print("Using lifter", LifterClass, "to lift", path)

    return lifter.lift(file_content)
