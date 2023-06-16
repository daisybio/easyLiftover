from rest_framework.response import Response
from pyliftover import LiftOver
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


def __process_bed__(file_content: str, from_ga: str, to_ga: str) -> str:
    """Lifts over a bed file.

    Args:
        file_content: The content of the bed file.
        from_ga: The genome assembly of the input file.
        to_ga: The genome assembly to lift over to.

    Returns:
        The content of the lifted over bed file.
    """
    lo = LiftOver(from_ga, to_ga)

    result = []

    for row in file_content.split("\n"):
        if row == "" or row.startswith("#"):
            continue

        chromosome, start, end, *rest = row.split()

        lifted_start = lo.convert_coordinate(chromosome, int(start))
        lifted_end = lo.convert_coordinate(chromosome, int(end))

        if lifted_start is None or lifted_end is None:
            continue

        if len(lifted_start) == 0 or len(lifted_end) == 0:
            continue

        result.append(
            "\t".join(
                [
                    lifted_start[0][0],
                    str(lifted_start[0][1]),
                    str(lifted_end[0][1]),
                    *rest,
                ]
            )
        )

    return "\n".join(result)


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
        method = __process_bed__
    else:
        raise Exception("Unsupported file type")
        
    uplifted_file_content = method(file_content, from_ga, to_ga)
    return Response(uplifted_file_content, content_type="text/plain")
