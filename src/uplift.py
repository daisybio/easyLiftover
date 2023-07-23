from .lifters import BedLifter, GffLifter, WigLifter, AbstractLifter

def uplift(
    fromGenome: str, toGenome: str, path: str, file_type: "str | None" = None
) -> str:
    """
    Uplifts a file from one genome build to another.

    Parameters:
        fromGenome (str): The genome build to lift from.
        toGenome (str): The genome build to lift to.
        path (str): The path to the file to lift.
        file_type (str): The type of the file to lift. If not provided, the file extension will be used.

    Returns:
        str: The lifted file content.
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

    lifter: AbstractLifter = LifterClass(fromGenome, toGenome)

    print("Using lifter", LifterClass, "to lift", path)

    return lifter.lift(file_content)
