from ._version import __version__

from .iloadmagics import CustomMagicsClass

def _jupyter_labextension_paths():
    return [{
        "src": "labextension",
        "dest": "iloadmagics"
    }]

try:
    ipy = get_ipython()
    ipy.register_magics(CustomMagicsClass)
    print(f"iloadmagics v{__version__}")

except AttributeError:
    print("Can not load imetacell because this is not a jupyter lab/notebook .ipynb file")