from .liftover import lifters

def get_file_types():
    return [format for lifter in lifters for format in lifter.supported_formats()]
