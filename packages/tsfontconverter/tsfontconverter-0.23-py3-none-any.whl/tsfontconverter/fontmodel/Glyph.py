from dataclasses import dataclass
from py_ts_interfaces import Interface


@dataclass
class Glyph(Interface):
    glyphId: int = -1
    unicode: str = ""
