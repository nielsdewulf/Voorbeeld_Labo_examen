class Adres:

    def __init__(self, straat, huisnummer, postcode, gemeente):
        self.straat = straat
        self.huisnummer = huisnummer
        self.postcode = postcode
        self.gemeente = gemeente

    @property
    def straat(self):
        return self.__straat

    @straat.setter
    def straat(self, value):
        if isinstance(value, str) and value is not "":
            self.__straat = value
        else:
            raise ValueError("Straat moet een string zijn")

    @property
    def huisnummer(self):
        return self.__huisnummer

    @huisnummer.setter
    def huisnummer(self, value):
        if isinstance(value, str) and value is not "":
            self.__huisnummer = value
        else:
            raise ValueError("Huisnummer moet een string zijn")

    @property
    def postcode(self):
        return self.__postcode

    @postcode.setter
    def postcode(self, value):
        if isinstance(value, str) and value is not "":
            self.__postcode = value
        else:
            raise ValueError("Postcode moet een string zijn")

    @property
    def gemeente(self):
        return self.__gemeente

    @gemeente.setter
    def gemeente(self, value):
        if isinstance(value, str):
            self.__gemeente = value
        else:
            raise ValueError("Gemeente moet een string zijn")

    def __eq__(self, other):
        return self.straat == other.straat and self.huisnummer == other.huisnummer and self.gemeente == other.gemeente and self.postcode == other.postcode

    def __lt__(self, other):
        if self.straat == other.straat:
            return self.huisnummer < other.huisnummer
        else:
            return self.straat < other.straat

    def __str__(self):
        return "{0} {1}, {2} {3}".format(self.straat, self.huisnummer, self.gemeente, self.postcode)
