from src.tsfontconverter.tsfontconverter import create_font_list
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
FONTDIRPATH = os.getenv("FONTDIRPATH")
OUTPUTPATH = os.getenv("OUTPUTPATH")


def test_tsfontconverter():
    create_font_list(fontdirpath=FONTDIRPATH,
                     outputpath=OUTPUTPATH)