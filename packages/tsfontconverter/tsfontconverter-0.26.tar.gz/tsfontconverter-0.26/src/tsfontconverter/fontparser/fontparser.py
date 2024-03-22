import os
import json
import base64

from fontTools.ttLib import TTFont

from ..fontmodel.CharacterMap import CharacterMap
from ..fontmodel.Font import Font

from ..fontmodel.Glyph import Glyph
from ..fontmodel.Meta import Meta


def create_font_info(glyphs_unicode, fontname, font_metadata):
    font = Font()
    font.name = fontname
    font.meta = font_metadata
    font.characterMap = CharacterMap()
    characterMap = {}
    for glyph, unicode_code in glyphs_unicode:
        characterMap[glyph] = unicode_code
    for glyphId in characterMap:
        glyph = Glyph()
        glyph.glyphId = glyphId
        glyph.unicode = characterMap[glyphId]
        font.characterMap.glyphs.append(glyph)
    return font


def extract_metadata(font):
    naming_table = font['name']
    font_metadata = Meta()
    for record in naming_table.names:
        if record.nameID == 2:  # Description
            font_metadata.description = record.toUnicode()
        elif record.nameID == 14:  # License URL
            font_metadata.licenseUrl = record.toUnicode()
        elif record.nameID == 12:  # Designer URL
            font_metadata.designerUrl = record.toUnicode()
        elif record.nameID == 11:  # Manufacturer URL
            font_metadata.manufacturerUrl = record.toUnicode()
        elif record.nameID == 10:  # Sample text
            font_metadata.sampleText = record.toUnicode()
    return font_metadata


def extract_glyphs_and_unicode(font):
    glyph_list = []

    # Check if the font is TrueType or CFF
    is_truetype = 'glyf' in font
    is_cff = 'CFF ' in font

    if is_truetype:
        cmap = font['cmap'].getBestCmap()
        for glyph_id, unicode_char in cmap.items():
            glyph_list.append((unicode_char, hex(glyph_id)))

    elif is_cff:
        for table in font['cmap'].tables:
            for code, name in table.cmap.items():
                glyph_list.append((name, hex(code)))
    return list(filter(lambda item: item is not None, glyph_list))


def read_font_file(file_path):
    font = TTFont(file_path)
    # Process the font file here
    return font


class FontParser:

    def __init__(self, outputpath, fontdirpath):
        print(f"FontParser initialized {outputpath} {fontdirpath}")
        self._outputpath = outputpath
        self._fontdirpath = fontdirpath

    @property
    def outputpath(self):
        return self._outputpath

    @outputpath.setter
    def outputpath(self, outputpath):
        self._outputpath = outputpath

    @property
    def fontdirpath(self):
        return self._fontdirpath

    @fontdirpath.setter
    def fontdirpath(self, fontdirpath):
        self._fontdirpath = fontdirpath

    def create_base64_encoded_data_uri(self, fontpath):
        with open(fontpath, "rb") as image_file:
            return f"data:font/opentype;base64,{base64.b64encode(image_file.read()).decode("utf-8")}"

    def list_font_files(self):
        myList = os.listdir(self._fontdirpath)
        fontinfolist = []
        for fontname in myList:
            fontpath = self._fontdirpath + "/" + fontname
            if fontpath.endswith(".ttf") or fontpath.endswith(".otf"):
                font = TTFont(fontpath)
                glyphs_unicode = extract_glyphs_and_unicode(font)
                fontinfo = create_font_info(glyphs_unicode, fontname, extract_metadata(font))
                fontinfo.dataUri = self.create_base64_encoded_data_uri(fontpath)
                fontinfolist.append(fontinfo)
        font_info_dicts = [font_info.to_dict() for font_info in fontinfolist]
        with open(self._outputpath, "w") as json_file:
            json_data = json.dumps(font_info_dicts, indent=1)
            json_file.write(json_data)
