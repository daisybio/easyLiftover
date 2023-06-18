from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json

@api_view(["GET"])
def get_genomes(req) -> Response:
    url = "https://api.genome.ucsc.edu/list/ucscGenomes"
    
    result = json.loads(requests.get(url).content)['ucscGenomes']
    
    return Response(result, content_type="application/json")
    