from .lifters import (
    BedLifter,
    GffLifter,
    WigLifter,
    AbstractLifter,
    BigWigLifter,
    BedGraphLifter,
    VcfLifter,
)

lifters = [BedLifter, GffLifter, WigLifter, BigWigLifter, BedGraphLifter, VcfLifter]

def get_lifter(
    fromGenome: str, toGenome: str, source: str, file_type: "str | None" = None
) -> AbstractLifter:
    def get_class(c_type):
        for lifter in lifters:
            if c_type in lifter.supported_formats():
                return lifter
            raise Exception("Unsupported file type: " + c_type)

    def __get_type(path: str) -> str:
        return path.split(".")[-1]

    chosen_type = file_type if file_type is not None else __get_type(source)

    clazz = get_class(chosen_type.lower())

    if clazz is None:
        raise Exception("Unsupported file type")

    return clazz(fromGenome, toGenome)


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
