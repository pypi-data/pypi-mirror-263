from src.fontparser.fontparser import FontParser

def convert_font(font):
    # Add your font conversion logic here
    print("converting font: {font}".format(font=str(font)))


def create_font_list(fontdirpath, outputpath):
    fontparser = FontParser(fontdirpath=fontdirpath, outputpath=outputpath)
    fontparser.list_font_files()
