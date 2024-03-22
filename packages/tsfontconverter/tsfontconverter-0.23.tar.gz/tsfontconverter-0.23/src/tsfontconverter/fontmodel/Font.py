from dataclasses import dataclass, field

from .CharacterMap import CharacterMap
from .Glyph import Glyph
from .Meta import Meta
from py_ts_interfaces import Interface


@dataclass
class Font(Interface):
    meta: Meta = field(default_factory=Meta)
    name: str = ""
    characterMap: CharacterMap = field(default_factory=CharacterMap)
    dataUri: str = ""

    def to_dict(self):
        meta = Meta().__dict__ if self.meta is None else self.meta.__dict__
        characterMap = CharacterMap().to_dict() if self.characterMap is None else self.characterMap.to_dict()
        return {
            "meta": meta,
            "name": self.name,
            "characterMap": characterMap,
            "dataUri": self.dataUri,
        }
