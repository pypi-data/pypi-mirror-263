"""
A scraper to collect paths from Renderman nodes.
"""
from __future__ import unicode_literals

from ciomaya.lib import scraper_utils


# See https://rmanwiki.pixar.com/display/RFM22/String+tokens+in+RfM
TOKENS = (r"_MAPID_", r"<udim>", r"<frame>", r"<f\d?>", r"<aov>", r"#+")

def run(_):
    return doit()

def doit(_=None):
    paths = scraper_utils.get_paths(scraper_utils.DIRMAP_MISSING_ATTRS['Renderman_For_Maya'])
    paths = scraper_utils.starize_tokens(paths, *TOKENS)
    paths = scraper_utils.expand_workspace(paths)
    paths = scraper_utils.extend_with_tx_paths(paths)
    return {"paths":paths, "env":[]}
