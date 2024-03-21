from src.fontmodel.FontMetadata import FontMetadata
class FontInfo:
    def __init__(self):
        self._name = None
        self._characterMap = {}
        self._meta = None
        self._dataUri = None

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def dataUri(self) -> str:
        return self._dataUri

    @name.setter
    def dataUri(self, dataUri: str):
        self._dataUri = dataUri


    @property
    def meta(self) -> FontMetadata:
        return self._meta

    @meta.setter
    def meta(self, value: FontMetadata):
        self._meta = value

    @property
    def characterMap(self) -> dict:
        return self._characterMap

    def add_glyph(self, glyph, unicode_code):
        self._characterMap[glyph] = unicode_code

    def to_dict(self):
        name = "" if self.name is None else self.name
        characterMap = {} if self.characterMap is None else self.characterMap
        meta = {} if self._meta is None else self.meta.to_dict()
        dataUri = "" if self._dataUri is None else self._dataUri
        return {
            "name": name,
            "numberOfGlyphs": len(self._characterMap),
            "characterMap": characterMap,
            "meta": meta,
            "dataUri": dataUri
        }
