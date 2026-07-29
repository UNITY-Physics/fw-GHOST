import sys
from unittest.mock import MagicMock

# utils.parser imports ghost.bids, which pulls in heavy scientific
# dependencies (ants, pybids, scikit-image) that aren't needed to unit
# test pure-logic helpers like make_session_label. Stub them out so
# these tests can run without the full gear Docker image installed.
for _module_name in (
    "ants",
    "bids",
    "bids.layout",
    "bids.layout.models",
    "skimage",
    "skimage.draw",
    "skimage.metrics",
    "SimpleITK",
):
    if _module_name not in sys.modules:
        sys.modules[_module_name] = MagicMock()
