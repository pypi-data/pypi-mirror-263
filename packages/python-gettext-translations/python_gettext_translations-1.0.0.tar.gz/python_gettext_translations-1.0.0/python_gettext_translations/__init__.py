__version_info__ = (1, 0, 0)
__version__ = "1.0.0"

def setup(app):
    return {"version": __version__, "parallel_read_safe": True}