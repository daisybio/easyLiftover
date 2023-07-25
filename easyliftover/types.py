import json
import os

def get_file_types():
    file_name = "types.json"
    
    script_dir = os.path.dirname(__file__)
    
    json_object = json.load(open(os.path.join(script_dir, file_name), "r"))
    
    return json_object