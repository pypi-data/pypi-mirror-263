__version_info__ = (0, 0, 1)
__version__ = "0.0.1"

def setup(app):
    return {"version": __version__, "parallel_read_safe": True}