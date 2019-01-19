from model.Handelszaak import Handelszaak
from model.Adres import Adres
import logging


class Huisartspraktijk(Handelszaak):

    def __init__(self, adr, telefoonnr, praktijktype):
        super().__init__(adr, telefoonnr)
        self.praktijktype = praktijktype
        self.huisartsen = []

    @property
    def praktijktype(self):
        return self.__praktijktype

    @praktijktype.setter
    def praktijktype(self, value):
        if isinstance(value, str) and value is not "":
            self.__praktijktype = value
        else:
            raise ValueError("Praktijktype moet een string zijn")

    def __str__(self):
        return "{0}: {1}".format(self.praktijktype, super().__str__())

    def voeg_huisarts_toe(self, arts):
        if isinstance(arts, str) and arts is not "":
            self.huisartsen.append(arts)
        else:
            raise ValueError("Arts moet in een string zijn")

    @staticmethod
    def inlezen_huisartsen(pad):
        resultaat = {}
        fo = open(pad, "r")
        for el in fo.readlines()[1:]:
            try:
                el = el.rstrip("\n")
                el = el.replace("\"", "")
                el = el.split(";")
                naam = el[1]
                huisnr = el[2]
                type = el[3]
                straat = el[4]
                gemeente = el[5]
                postcode = el[6]
                telefoonnr = el[8]

                adr = Adres(straat, huisnr, postcode, gemeente)
                if adr.__str__() in resultaat:
                    resultaat[adr.__str__()].voeg_huisarts_toe(naam)
                else:
                    praktijk = Huisartspraktijk(adr, telefoonnr, type)
                    praktijk.voeg_huisarts_toe(naam)
                    resultaat[adr.__str__()] = praktijk
            except Exception as st:
                logging.debug("Lijn niet kunnen inlezen")

        fo.close()
        return resultaat.values()

    @staticmethod
    def print_info_alle_praktijken(praktijken):
        for el in praktijken:
            if isinstance(el, Huisartspraktijk):
                print(el)
                for arts in el.huisartsen:
                    print("\tArts: {0}".format(arts))

    @staticmethod
    def zoek_info_arts(praktijken, naam):
        for praktijk in praktijken:
            for arts in praktijk.huisartsen:
                if arts.find(naam) != -1:
                    return praktijk
