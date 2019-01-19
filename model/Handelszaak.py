from model.Adres import Adres
import logging


class Handelszaak:

    def __init__(self, adres, telefoonnr):
        self.adres = adres
        self.telefoonnr = telefoonnr

    @property
    def adres(self):
        return self.__adres

    @adres.setter
    def adres(self, value):
        if isinstance(value, Adres) and value is not "":
            self.__adres = value
        else:
            raise ValueError("Geen adres ingegeven via de Klasse Adres")

    @property
    def telefoonnr(self):
        return self.__telefoonnr

    @telefoonnr.setter
    def telefoonnr(self, value):
        if isinstance(value, str) and value is not "":
            self.__telefoonnr = value
        else:
            raise ValueError("Telefoonnummer moet in String zijn")

    def __str__(self):
        return "Adres {0}: Tel {1}".format(self.adres, self.telefoonnr)

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass
