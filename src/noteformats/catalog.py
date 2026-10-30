"""Shared current classification and exact generated-geometry counts."""

from collections import defaultdict

from .geometry import Scene
from .registry import BUILDERS
from .reviews import geometry_digest
from .variants import ORIGINAL_MERGES, RECLASSIFIED_HEADERS, VARIANT_METHODS

VARIANTS = {
    **{key: {**value, "classification": VARIANT_METHODS[key][0]}
       for key, value in ORIGINAL_MERGES.items() if VARIANT_METHODS[key][0] != "independent"},
    **{key: {"target": value, "classification": "parameter", "reason": "Shared question band parameter."}
       for key, value in RECLASSIFIED_HEADERS.items()},
}


def geometry_groups(profile: dict) -> dict[str, list[str]]:
    groups = defaultdict(list)
    for layout_id, builder in BUILDERS.items():
        scene = Scene.from_profile(profile)
        builder(scene, profile)
        groups[geometry_digest(scene)].append(layout_id)
    return dict(groups)


def counts(profile: dict) -> dict:
    groups = geometry_groups(profile)
    return {"ids": len(BUILDERS), "base_formats": len(BUILDERS) - len(VARIANTS),
            "variants": len(VARIANTS), "unique_geometry": len(groups),
            "shared_geometry_groups": sum(len(ids) > 1 for ids in groups.values())}
