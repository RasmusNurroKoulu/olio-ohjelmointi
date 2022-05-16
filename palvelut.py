import random

class Asiakas:
    """Luokka, joka antaa asiakkaalle nimen, numeron, iän ja luo numeron
    
    Julkiset methodit:
    """

    def _luo_nro(self):
        """Luo asiakkaan numeron.
        :param n1: antaa 1 numeron
        :type n1: int
        :param n2: antaa 2 numeron
        :type n2: int
        :param n3: antaa 3 numeron
        :type n3: int
        :param n4: antaa 4 numeron
        :type n4: int
        :param n5: antaa 5 numeron
        :type n5: int
        :param n6: antaa 6 numeron
        :type n6: int
        :param n7: antaa 7 numeron
        :type n7: int
        :param n8: antaa 8 numeron
        :type n8: int
        :return: koko numero
        :rtype str
        """
        n1 = random.randint(0, 9)
        n2 = random.randint(0, 9)
        n3 = random.randint(0, 9)
        n4 = random.randint(0, 9)
        n5 = random.randint(0, 9)
        n6 = random.randint(0, 9)
        n7 = random.randint(0, 9)
        n8 = random.randint(0, 9)
        return "f'{n1}{n2}-{n3}{n4}{n5}-{n6}{n7}{n8}'"

    def __init__(self, nimi, ika):
        """Luo asiakkaan tiedot.
        :param nimi: antaa nimen
        :type nimi: str
        :param _asiakasnro: antaa asiakas numeron
        :type _asiakasnro: int
        :param _ika: antaa iän
        :type _ika: int
        """
        self.__nimi = nimi, str
        self.__ika = ika, int
        self.__asiakasnro = self._luo_nro()

    def get_nimi(self):
        """Palauttaa nimen.
        :return: asiakkaan nimi
        :rtype: str
        """
        try: 
            return self.__nimi
        except NameError:
            print("Suosittelen antamaan uuden nimen")

    def set_nimi(self, uusi_nimi):
        """Asettaa uuden nimen.
        :param nimi: antaa nimen
        :type nimi: str
        """
        try:
            if uusi_nimi != "":
                self.__nimi = uusi_nimi
        except ValueError:
            print("Anna uusi nimi")

    def get_ika(self):
        """Palauttaa iän.
        :return: asiakkaan ikä
        :rtype: int
        """
        try:
            return self.__ika
        except ValueError:
            print("Kehotan antamaan uuden nimen ja iän")

    def set_ika(self, uusi_ika):
        """Asettaa uuden iän.
        :param _ika: antaa iän
        :type _ika: int
        :param uusi_ika: uusi ikä
        :type uusi_ika: int
        """
        try:
            if uusi_ika != "":
                self.__ika = uusi_ika
        except ValueError:
            print("Anna kunnon ikä")

    def get_nro(self):
        """Palauttaa asiakkaan numeron.
        :return: asiakkaan numero
        :rtype: str
        """
        return self.__asiakasnro

class Palvelu(Asiakas):
    """Luokka, millä voit muokata asiakkaita 
    
    Julkiset methodit:
        lisaa_asiakas(_asiakkaat)
        tulosta_asiakkaat()
    """
    def __init__(self, tuotenimi):
        """Luo tuotenimen ja hakee asiakkaat.
        :param tuotenimi: antaa tuotenimen
        :type tuotenimi: str
        :param __asiakkaat: antaa asiakas numeron
        :type __asiakkaat: int
        :param __asiakkaat: hakee asiakkaat
        :type __asiakkaat: Union[int, float]
        """
        self.tuotenimi = tuotenimi
        self.__asiakkaat = []

    def _luo_asiakasrivi(__asiakkaat):
        """Palauttaa asiakkaan.
        :return: asiakkas
        :rtype: str
        """
        return "f'{__asiakkaat.get_nimi()} on asiakkaamme'"
    def lisaa_asiakas(self, nimi, ika = 0):
        """Lisää asiakkaat listaan
        :param __asiakkaat: hakee asiakkaat
        :type __asiakkaat: Union[int, float]
        """
        try:
            if nimi and ika != "":
                self.__asiakkaat.append(Asiakas(nimi, ika))
        except ValueError:
            print("Anna kunnon tiedot")

    def poista_asiakas(__asiakkaat, poistettava):
        """Poistaa asiakkaat listaan
        :param __asiakkaat: hakee asiakkaat
        :type __asiakkaat: Union[int, float]
        """
        try:
            __asiakkaat.remove(poistettava)
        except ValueError:
            pass

    def tulosta_asiakkaat(self):
        for x in range(len(self.__asiakkaat)):
            print(self.__asiakkaat[x])


class ParempiPalvelu(Palvelu):
    """Luokka, mikä on parempi palvelu, kun normaali 
    
    Julkiset methodit:
        lisaa_etu(),
        poista_etu(),
        tulosta_edut()
    """
    def __init__(self, tuotenimi):
        """Ottaa edut tuotteesta
        :param __edut: asettaa edut tuotenimi listaksi
        :type __edut: str
        """
        super().__init__(tuotenimi)
        self.__edut = [tuotenimi]
    
    def lisaa_etu(self, _etu):
        """Lisää etu listaan
        :param __edut: hakee asiakkaat
        :type __edut: Union[int, float]
        """
        try:
            self.__edut.append(_etu)
        except ValueError:
            print("Anna kunnon tiedot")

    
    def poista_etu(self, poistettava):
        """Poistaa etu listaan
        :param __edut: hakee asiakkaat
        :type __edut: Union[int, float]
        """
        try:
            self.__edut.remove(poistettava)
        except ValueError:
            pass

    def tulosta_edut(self):
        """Tulosta etu listan
        :param __edut: hakee asiakkaat
        :type __edut: Union[int, float]
        """
        for x in range(len(self.__edut)):
            print(self.__edut[x])
