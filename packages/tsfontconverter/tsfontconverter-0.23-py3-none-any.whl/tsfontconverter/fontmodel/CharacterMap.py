from dataclasses import dataclass, field
from typing import List
from py_ts_interfaces import Interface

from .Glyph import Glyph


@dataclass
class CharacterMap(Interface):

    glyphs: List[Glyph] = field(default_factory=list)

    def to_dict(self):
        glyphs = [] if self.glyphs is None else [glyph.__dict__ for glyph in self.glyphs]
        return {
            "glyphs": glyphs
        }