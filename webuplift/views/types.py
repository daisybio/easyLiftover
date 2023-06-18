from rest_framework.response import Response
from rest_framework.decorators import api_view
from webuplift.views.lifters import *


@api_view(["GET"])
def get_types(req) -> Response:
    """Gets the supported file types.

    Args:
        req: The request object.

    Returns:
        A response object with the supported file types.
    """
    return Response(
        [
            {
                "name": "Annotation",
                "Description": "Non-quantiative annotation file",
                "formats": [
                    {"name": "bed", "can_be_lifted": True},
                    {"name": "gff", "can_be_lifted": True},
                    {"name": "gff3", "can_be_lifted": True},
                    {"name": "gtf", "can_be_lifted": True},
                    {"name": "bedpe", "can_be_lifted": False},
                    {"name": "Other", "can_be_lifted": False},
                ],
            },
            {
                "name": "Wiggle",
                "Description": "Quantitative genomic data",
                "formats": [
                    {"name": "wig", "can_be_lifted": True},
                    {"name": "bigWig", "can_be_lifted": False},
                    {"name": "bedGraph", "can_be_lifted": False},
                    {"name": "Other", "can_be_lifted": False},
                ],
            },
        ],
        content_type="application/json",
    )
