from __future__ import unicode_literals
import re
import sys
from contextlib import contextmanager

import pymel.core as pm
from ciomaya.lib import scraper_utils
from ciomaya.lib.ae import AEcommon
from ciopath.gpath import Path


DRIVE_LETTER_RX = re.compile(r"^([a-zA-Z]):.*")

ATTRS = {
    "Renderman_for_Maya": {
        "PxrBump": ["filename"],
        "PxrCookieLightFilter": ["map"],
        "PxrDiskLight": ["iesProfile"],
        "PxrDomeLight": ["lightColorMap"],
        "PxrGobo": ["map"],
        "PxrGoboLightFilter": ["map"],
        "PxrLayeredTexture": ["maskTexture", "filename"],
        "PxrMultiTexture": [
            "filename0",
            "filename1",
            "filename2",
            "filename3",
            "filename4",
            "filename5",
            "filename6",
            "filename7",
            "filename8",
            "filename9",
        ],
        "PxrNormalMap": ["filename"],
        "PxrOSL": ["shadername"],
        "PxrProjectionLayer": ["channelsFilenames", "filename"],
        "PxrPtexture": ["filename"],
        "PxrRectLight": ["lightColorMap", "iesProfile"],
        "PxrSphereLight": ["iesProfile"],
        "PxrStdAreaLight": ["profileMap", "rman__EmissionMap", "iesProfile", "barnDoorMap"],
        "PxrStdEnvMapLight": ["rman__EnvMap"],
        "PxrTexture": ["filename"],
        "PxrVisualizer": ["matCap"],
        "RenderManArchive": ["filename"],
        "rmanImageFile": ["File"],
        "rmanTexture3d": ["File"],
        "RMSAreaLight": ["mapname"],
        "RMSCausticLight": ["causticPhotonMap"],
        "RMSEnvLight": ["rman__EnvMap"],
        "RMSGPSurface": [
            "SpecularMapB",
            "SpecularMap",
            "RoughnessMap",
            "MaskMap",
            "SurfaceMap",
            "DisplacementMap",
        ],
        "RMSGeoAreaLight": ["profilemap", "iesprofile", "lightcolormap", "barnDoorMap"],
        "RMSGeoLightBlocker": ["Map"],
        "RMSGlass": ["roughnessMap", "surfaceMap", "specularMap", "displacementMap"],
        "RMSLightBlocker": ["Map"],
        "RMSMatte": ["SurfaceMap", "MaskMap", "DisplacementMap"],
        "RMSOcean": ["roughnessMap", "surfaceMap", "specularMap", "displacementMap"],
    }
}



strip_drive = scraper_utils.strip_drive