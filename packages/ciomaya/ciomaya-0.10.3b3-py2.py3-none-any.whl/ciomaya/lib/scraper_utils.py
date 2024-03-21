from __future__ import unicode_literals
import os
import re
import sys
import importlib
from contextlib import contextmanager

from cioseq.sequence import Sequence

from ciopath.gpath import Path

import maya.api.OpenMaya as om
from ciomaya.lib.ae import AEcommon
import pymel.core as pm

PLATFORM = sys.platform
PLACEHOLDER = "CIOPLACEHOLDER"  # Can be anything unique.
ATTR_TOKEN_REGEX = re.compile(
    r"<attr:([0-9a-zA-Z_]+)(?:\s+index:([0-9]+))?(?:\s+default:([0-9a-zA-Z_]+))?>"
)

DRIVE_LETTER_RX = re.compile(r"^([a-zA-Z]):.*")

RENDERMAN_ATTRS = {
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

XGEN_ATTRS = { "xgmSplineCache" :["fileName"] }


def get_paths(attrs):
    """
    Get paths from attributes.

    First get the plugs and iterate. If the leaf level plug is an array, then we
    find out with isArray() and iterate over its elements.

    """
    result = []
    plug_list = _get_plugs(attrs)
    plug_iter = om.MItSelectionList(plug_list)
    while not plug_iter.isDone():
        plug = plug_iter.getPlug()
        plug_iter.next()

        if plug.isArray:
            for index in range(plug.numElements()):
                child_plug = plug.elementByPhysicalIndex(index)
                obj = _get_value(child_plug)
                if obj:
                    result.append(obj)
        else:
            obj = _get_value(plug)
            if obj:
                result.append(obj)

    return result


def get_sequence(node):
    node = pm.PyNode(node)  # just in case
    use_custom_range = node.attr("useCustomRange").get()
    if use_custom_range:
        custom_range = node.attr("frameSpec").get()
        return Sequence.create(custom_range)

    if node.attr("animation").get():
        start_frame = node.attr("startFrame").get()
        end_frame = node.attr("endFrame").get()
        by_frame = node.attr("byFrame").get()
        return Sequence.create(int(start_frame), int(end_frame), by_frame)

    return Sequence.create(int(pm.currentTime(q=True)))



def _get_plugs(attrs):
    """
    Return a SelectionList that contains the actual existing plugs.

    When we get a node's plug from the att name, it may be a child of a compound
    array plug (or nested several levels). In this case the plug name will be of
    the form node_name.parentPlug[-1].childPlug This (-1) is a nonexistent plug.
    In order to get the actual plug elements, if they exist, we use a
    SelectionList. We add a wildcard name to the selectionlist to get the real
    plugs it contains.

    The [-1] indicator is only used for array parent plugs, not leaf level array
    plugs.

    [
        "someGrouping": {
            "someNodeType": [
                "topLevelAttributeName",
                "nestedAttributeName",
                "arrayTypeAttributeName",
                "childOfNestedArrayTypeAttributeName"
            ],
            ...
        },
        ...
    ]
    """
    all_node_types = pm.allNodeTypes()
    selection_list = om.MSelectionList()
    for nodetype in attrs:
        if nodetype in all_node_types:
            for node in pm.ls(type=nodetype):
                for attr in attrs[nodetype]:
                    try:
                        selection_list.add(
                            node.attr(attr).name().replace("[-1]", "[*]")
                        )
                    except (RuntimeError, pm.MayaAttributeError):
                        pass
    return selection_list


def _get_value(plug):
    value = plug.asString()
    if value:
        return {"path": value, "plug": plug.name()}


def starize_tokens(paths, *tokens):
    """
    Replace any of the given tokens with a '*'

    Accepts either a list of objects with a path property, or a list of strings.
    """
    token_rx = re.compile("|".join(tokens), re.IGNORECASE)
    for i in range(len(paths)):
        try:
            paths[i]["path"] = token_rx.sub("*", paths[i]["path"])
        except TypeError:
            paths[i] = token_rx.sub("*", paths[i])
    return paths


def expand_env_vars(paths):
    """Use Path() to resolve env vars.

    Accepts either a list of objects with a path property, or a list of strings.
    """
    for i in range(len(paths)):
        try:
            paths[i]["path"] = Path(paths[i]["path"]).fslash()
        except TypeError:
            paths[i] = Path(paths[i]).fslash()
    return paths


def expand_workspace(paths):
    """
    Expand in a non-platform-dependent way.

    Paths are either a list of strings, a list of objects with a "path" key, or
    a mix.

    Sometimes on a Mac/Linux, the user will have a scene with Windows paths in
    it. That's a mistake of course, but we want to show them the mistake. If we
    just expandName, then those windows paths will be treated as relative. The
    expandName function prepends the workspace, and to add insult to injury, it
    deletes everything after the drive letter. You end up with
    /Volumes/blah/blah/C So we check that its absolute before running through
    expandName and we leave it in tact with its drive letter so the user can
    identify it during validation.

    If any empty paths turn up here, then remove them, because whan an empty path
    gets prepended by the workspace, we end up with the whole project uploaded.
    """
    ws = pm.Workspace()
    result = []

    for p in paths:
        try:
            if p["path"]:
                if Path(p["path"]).relative:
                    p.update({"path": ws.expandName(p["path"])})
                    result.append(p)
                else:
                    result.append(p)
        except (TypeError, KeyError):
            if p:
                if Path(p).relative:
                    result.append(ws.expandName(p))
                else:
                    result.append(p)

    return result


def extend_with_tx_paths(paths):
    """
    Add the tx sister for image files

    Use glob notation around one letter in the extension (.t[x]) because when
    paths are finally resolved, the list is expanded by globbing.

    As TX files are not critical, we don't want to show a warning if they
    don't exist. Glob will ultimately expand to no files if the file does not
    exist, and therefore not complain.
    """

    image_ext_regex = re.compile(
        r"^\.(jpg|jpeg|gif|iff|psd|png|pic|tga|tif|tiff|bmp|hdr|sgi|rla|exr|ico|dpx|cin)$",
        re.IGNORECASE
    )
    txpaths = []
    for p in paths:
        root, ext = os.path.splitext(p["path"])
        if image_ext_regex.match(ext):
            txpath = "{}.t[x]".format(root)
            txpaths.append({"plug": p["plug"], "path": txpath})
    return paths + txpaths


def resolve_to_sequence(template, sequence):
    """
    Replace all the popular frame placeholders with a consistent template
    expression that specifies the padding
    """

    orig_template = template
    # replace 4 hashes with  {frame:04d}
    template = re.compile(r"(#+)", re.IGNORECASE).sub(
        lambda match: "{{frame:0{:d}d}}".format(len(match.group(1))), template
    )

    # replace $F4 with {frame:04d}
    template = re.compile(r"\$F(\d?)", re.IGNORECASE).sub(
        lambda match: "{{frame:0{:d}d}}".format(int(match.group(1) or "1")), template
    )

    # replace <f4> with {frame:04d}
    template = re.compile(r"<F(\d?)>", re.IGNORECASE).sub(
        lambda match: "{{frame:0{:d}d}}".format(int(match.group(1) or "1")), template
    )

    # replace <frame> with {frame}
    template = re.compile(r"<frame>", re.IGNORECASE).sub("{frame}", template)

    if orig_template == template:
        return [orig_template]

    return sequence.expand_format(template)


def extract_attr_token(filename):
    """
    Find <attr: token in  paths specified like so:

    /Volumes/xtr/gd/standin_fixture//sourceimages/<attr:floormap default:alcazar>.jpg

    # https://docs.arnoldrenderer.com/pages/viewpage.action?pageId=40110953

    # REGEX TESTER
    # https://regex101.com/r/eFp4RT/1/
    #"""
    match = ATTR_TOKEN_REGEX.search(filename)
    if not match:
        return

    # cant do indices
    if match.group(2) is not None:
        return

    attr_name = match.group(1)
    default_val = match.group(3)
    template = ATTR_TOKEN_REGEX.sub(PLACEHOLDER, filename)

    return template, attr_name, default_val


# Create a custom exception to raise when a scraper fails.
class ScraperError(Exception):
    pass


def run_scrapers(node, scripts):
    """
    Run the scraper scripts.
    
    If there's a problem with any script, raise a ScraperError.
    """
    result = {"paths": [], "env": []}
    for script in scripts:
        try:
            scraper_module = importlib.import_module(script)
            try:
                reload(scraper_module)
            except NameError:
                importlib.reload(scraper_module)
            scraper_result = scraper_module.run(node)
            if scraper_result:
                result["paths"] += scraper_result["paths"]
                result["env"] += scraper_result["env"]
        except SyntaxError as exc:
            raise ScraperError(
                "Syntax error in the scraper script: '{}'.".format(script)
            )
        except ImportError as exc:
            raise ScraperError(
                "Can't load the script '{}' as a Python module.".format(script)
            )
        except BaseException as exc:
            raise ScraperError(
                "Unknown problem with the script '{}'.".format(script)
            )
    return result

@contextmanager
def strip_drive(attribute_map):
    '''
    Removes the drive letter from the give attributes
    
    :param attribute_map: A map of node types and which attributes
                          contain file paths
    :type attribute_map:
    '''

    if not sys.platform == "win32":
        yield
        return
        
    rx = re.compile(r"^([a-zA-Z]):.*")

    path_dicts = get_paths(attribute_map)

    pm.displayInfo( "Stripping {} attributes of their drive letter".format(len(path_dicts)))

    some_changed = False
    for p in path_dicts:

        if not DRIVE_LETTER_RX.match(p["path"]):
            continue
        try:
            pm.Attribute(p["plug"]).set(Path(p["path"]).fslash(with_drive=False))
            AEcommon.print_setAttr_cmd(p["plug"])
            some_changed = True

        except (ValueError, TypeError):
            pm.displayWarning(
                "Can't make the plug/path relative '{}'/'{}'".format(p["plug"], p["path"])
            )
            continue
    try:
        yield
    finally:
        if not some_changed:
            return
        pm.displayInfo( "Reverting...")
        for p in path_dicts:
            if not DRIVE_LETTER_RX.match(p["path"]):
                continue
            try:
                pm.Attribute(p["plug"]).set(p["path"])
                AEcommon.print_setAttr_cmd(p["plug"])
            except (ValueError, TypeError):
                pm.displayWarning(
                    "Can't revert the plug/path '{}'/'{}'".format(p["plug"], p["path"])
                )
                continue
