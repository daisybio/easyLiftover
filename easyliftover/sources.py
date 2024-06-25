import json
import os


def get_sources():
    file_name = "sources.json"

    script_dir = os.path.dirname(__file__)

    return json.load(open(os.path.join(script_dir, file_name), "r"))
