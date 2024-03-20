from src.tsfontconverter.tsfontconverter import TSFontConverter
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
FONTDIRPATH = os.getenv("FONTDIRPATH")
OUTPUTPATH = os.getenv("OUTPUTPATH")

def test_tsfontconverter():
    tsfc = TSFontConverter()
    tsfc.create_font_list(fontdirpath=FONTDIRPATH,
                          outputpath=OUTPUTPATH)

