from fontTools.ttLib import TTFont
from src.fontmodel.FontInfo import FontInfo
from src.fontmodel.FontMetadata import FontMetadata
import os
import json
import re


class FontParser:

    def __init__(self, outputpath, fontdirpath):
        print(
            "FontParser initialized {outputpath} {fontdirpath}".format(outputpath=outputpath, fontdirpath=fontdirpath))
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

    def read_font_file(self, file_path):
        font = TTFont(file_path)
        # Process the font file here
        return font

    def extract_glyphs_and_unicode(self, font):
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

    def create_font_info(self, glyphs_unicode, fontname, font_metadata):
        font_info = FontInfo()
        font_info.name = fontname
        font_info.meta = font_metadata
        for glyph, unicode_code in glyphs_unicode:
            try:
                font_info.add_glyph(glyph, unicode_code)
            except:
                print("could not add " + str(glyph))
        return font_info

    def extract_metadata(self, font):
        font_metadata = FontMetadata()
        naming_table = font['name']
        for record in naming_table.names:
            if record.nameID == 2:  # Description
                font_metadata.description = record.toUnicode()
            elif record.nameID == 14:  # License URL
                font_metadata.license_url = record.toUnicode()
            elif record.nameID == 12:  # Designer URL
                font_metadata.designer_url = record.toUnicode()
            elif record.nameID == 11:  # Manufacturer URL
                font_metadata.manufacturer_url = record.toUnicode()
            elif record.nameID == 10:  # Sample text
                font_metadata.sample_text = record.toUnicode()

        return font_metadata

    def list_font_files(self):
        myList = os.listdir(self._fontdirpath)
        fontinfolist = []
        for fontname in myList:
            fontpath = self._fontdirpath + "/" + fontname
            if fontpath.endswith(".ttf") or fontpath.endswith(".otf"):
                font = TTFont(fontpath)
                glyphs_unicode = self.extract_glyphs_and_unicode(font)
                fontinfo = self.create_font_info(glyphs_unicode, fontname, self.extract_metadata(font))
                fontinfolist.append(fontinfo)
        font_info_dicts = [font_info.to_dict() for font_info in fontinfolist]
        with open(self._outputpath, "w") as json_file:
            json_data = json.dumps(font_info_dicts, indent=1)
            json_data_single_line_glyphs = re.sub(r'"characterMap":\s*{(?:.|\n)*?}',
                                                  lambda m: m.group().replace('\n', ''), json_data, flags=re.DOTALL)
            json_file.write(json_data_single_line_glyphs)
