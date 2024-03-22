import inspect
import json
from typing import List

#from ..fontmodel.CharacterMap import CharacterMap
#rom ..fontmodel.Font import Font
from src.tsfontconverter.fontmodel.CharacterMap import CharacterMap
from src.tsfontconverter.fontmodel.Font import Font
from src.tsfontconverter.fontmodel.Glyph import Glyph
from src.tsfontconverter.fontmodel.Meta import Meta

from src.tsfontconverter.typescript.pytsconverter import convert_subscript_type
from src.tsfontconverter.typescript.pytsconverter import convert_regular_type

#from ..fontmodel.Glyph import Glyph
#from ..fontmodel.Meta import Meta


class NoQuoteEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def encode(self, o):
        if isinstance(o, (dict, list, tuple)):
            return super().encode(o)
        elif isinstance(o, (int, float)):
            return str(o)
        else:
            return o

def getClassDefinition(clazz):
    fontClassDefinition = inspect.signature(clazz.__init__)
    fontDict = {}
    for param_name, param in fontClassDefinition.parameters.items():
        if param_name is not "self":
            #fontDict[param_name] = param.annotation.__name__
            param_type = param.annotation
            if hasattr(param_type, "__origin__") and param_type.__origin__ == list:
                list_item_type = param_type.__args__[0].__name__
                tstype = convert_subscript_type(pytype=param.annotation.__name__, subsripttype=str(list_item_type))
                fontDict[param_name] = str(tstype)
            else:
                tstype = convert_regular_type(param.annotation.__name__)
                fontDict[param_name] = str(tstype)
    return f"export interface {clazz.__name__} {json.dumps(fontDict, indent=2).replace("\"", "")}"

def getAllDefinitions():
    return [getClassDefinition(cls) for cls in [Glyph, CharacterMap, Meta, Font]]

