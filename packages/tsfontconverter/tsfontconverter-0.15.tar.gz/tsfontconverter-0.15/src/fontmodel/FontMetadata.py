class FontMetadata:
    def __init__(self):
        self._description = None
        self._license_url = None
        self._designer_url = None
        self._manufacturer_url = None
        self._sample_text = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def license_url(self):
        return self._license_url

    @license_url.setter
    def license_url(self, value):
        self._license_url = value

    @property
    def designer_url(self):
        return self._designer_url

    @designer_url.setter
    def designer_url(self, value):
        self._designer_url = value

    @property
    def manufacturer_url(self):
        return self._manufacturer_url

    @manufacturer_url.setter
    def manufacturer_url(self, value):
        self._manufacturer_url = value

    @property
    def sample_text(self):
        return self._sample_text

    @sample_text.setter
    def sample_text(self, value):
        self._sample_text = value

    def to_dict(self):
        description = "" if self.description is None else self.description
        license_url = "" if self.license_url is None else self.license_url
        designer_url = "" if self.designer_url is None else self.designer_url
        manufacturer_url = "" if self.manufacturer_url is None else self.manufacturer_url
        sample_text = "" if self.sample_text is None else self.sample_text
        return {
            "description": description,
            "licenseUrl": license_url,
            "designerUrl": designer_url,
            "manufacturerUrl": manufacturer_url,
            "sampleText": sample_text
        }
