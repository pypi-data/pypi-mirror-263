from dataclasses import dataclass
from py_ts_interfaces import Interface


@dataclass
class Meta(Interface):

    designerUrl: str = ""
    licenseUrl: str = ""
    manufacturerUrl: str = ""
    description: str = ""
    sampleText: str = ""
