"""One entry point for implemented geometry builders."""

from .layouts.gate1 import BUILDERS as GATE1
from .layouts.foundation import BUILDERS as FOUNDATION
from .layouts.grid_dot import BUILDERS as GRID_DOT
from .layouts.geometry_paper import BUILDERS as GEOMETRY_PAPER
from .layouts.columns import BUILDERS as COLUMNS
from .layouts.cards import BUILDERS as CARDS
from .layouts.comparison import BUILDERS as COMPARISON
from .layouts.matrix import BUILDERS as MATRIX
from .layouts.mandala import BUILDERS as MANDALA
from .layouts.flow import BUILDERS as FLOW
from .layouts.causal import BUILDERS as CAUSAL
from .layouts.concept_network import BUILDERS as CONCEPT_NETWORK
from .layouts.hierarchy import BUILDERS as HIERARCHY
from .layouts.learning import BUILDERS as LEARNING
from .layouts.research import BUILDERS as RESEARCH
from .layouts.ideation import BUILDERS as IDEATION
from .layouts.storyboard_extra import BUILDERS as STORYBOARD_EXTRA
from .layouts.special_paper import BUILDERS as SPECIAL_PAPER
from .layouts.hybrid import BUILDERS as HYBRID

CANONICAL_BUILDERS = {**GATE1, **FOUNDATION, **GRID_DOT, **GEOMETRY_PAPER, **COLUMNS, **CARDS, **COMPARISON, **MATRIX, **MANDALA, **FLOW, **CAUSAL, **CONCEPT_NETWORK, **HIERARCHY, **LEARNING, **RESEARCH, **IDEATION, **STORYBOARD_EXTRA, **SPECIAL_PAPER, **HYBRID}

if len(CANONICAL_BUILDERS) != sum(len(x) for x in (GATE1, FOUNDATION, GRID_DOT, GEOMETRY_PAPER, COLUMNS, CARDS, COMPARISON, MATRIX, MANDALA, FLOW, CAUSAL, CONCEPT_NETWORK, HIERARCHY, LEARNING, RESEARCH, IDEATION, STORYBOARD_EXTRA, SPECIAL_PAPER, HYBRID)):
    raise RuntimeError("Duplicate builder ID")

from .variants import VARIANT_METHODS, make_variant_builders

BUILDERS = {**CANONICAL_BUILDERS, **make_variant_builders(CANONICAL_BUILDERS)}
if len(BUILDERS) != len(CANONICAL_BUILDERS) + len(VARIANT_METHODS):
    raise RuntimeError("Duplicate variant builder ID")
