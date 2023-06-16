from rest_framework.response import Response
from rest_framework.decorators import api_view
from webuplift.views.lifters import *


@api_view(["POST"])
def uplift(req) -> Response:
    """Uplifts a genomic position from one genome build to another.

    Args:
        req: The request object.

    Returns:
        A response object with the uplifted position.
    """
    # Get the parameters from the request.
    data = req.GET
    get_type = data.get("type", None)
    from_ga = data.get("from", None)
    to_ga = data.get("to", None)

    file = req.FILES.get("file", None)

    file_content = file.read().decode("utf-8")
    file_name = file.name
    file_extension = file_name.split(".")[-1]

    used_type = get_type if get_type is not None else file_extension

    if used_type == "bed":
        LifterClass = BedLifter
    elif used_type in ["gff", "gff3", "gtf"]:
        LifterClass = GffLifter
    else:
        raise Exception("Unsupported file type")

    print("Initializing lifter", LifterClass, "with", from_ga, to_ga)

    lifter = LifterClass(from_ga, to_ga)

    print("Using lifter", LifterClass, "to lift", file_name)

    return Response(lifter.lift(file_content), content_type="text/plain")
