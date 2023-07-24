from .lifters import BedLifter, GffLifter, WigLifter, AbstractLifter
import requests

def __get_type(path: str) -> str:
    return path.split(".")[-1]

def upliftUrl(
    fromGenome: str, toGenome: str, url: str, file_type: "str | None" = None
) -> str:
    chosen_type = file_type if file_type is not None else __get_type(url)
    return uplift(fromGenome, toGenome, requests.get(url).text, chosen_type)

def upliftPath(
    fromGenome: str, toGenome: str, path: str, file_type: "str | None" = None
) -> str:
    chosen_type = file_type if file_type is not None else __get_type(path)
    return uplift(fromGenome, toGenome, open(path, "r").read(), chosen_type)

def uplift(
    fromGenome: str, toGenome: str, content: str, file_type: str
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

    if file_type == "bed":
        LifterClass = BedLifter
    elif file_type in ["gff", "gff3", "gtf"]:
        LifterClass = GffLifter
    elif file_type == "wig":
        LifterClass = WigLifter
    else:
        raise Exception("Unsupported file type")

    print("Initializing lifter", LifterClass, "with", fromGenome, toGenome)

    lifter: AbstractLifter = LifterClass(fromGenome, toGenome)

    print("Using lifter", LifterClass, "with", fromGenome, toGenome)

    return lifter.lift(content)
