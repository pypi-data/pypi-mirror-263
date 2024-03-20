from src.fontparser.fontparser import FontParser


class TSFontConverter:
    def __init__(self):
        print("TSFontConverter initialized")

    def convert_font(self, font):
        # Add your font conversion logic here
        print("converting font: {font}".format(font=str(font)))

    def create_font_list(self, fontdirpath, outputpath):
        fontparser = FontParser(fontdirpath=fontdirpath, outputpath=outputpath)
        fontparser.list_font_files()


