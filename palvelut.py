import random

class Asiakas:
    """Luokka, joka antaa asiakkaalle nimen, numeron, iän ja luo numeron
    
    Julkiset methodit:
    """

    def _luo_nro(self):
        n1 = random.randint(0, 9)
        n2 = random.randint(0, 9)
        n3 = random.randint(0, 9)
        n4 = random.randint(0, 9)
        n5 = random.randint(0, 9)
        n6 = random.randint(0, 9)
        n7 = random.randint(0, 9)
        n8 = random.randint(0, 9)
        return f'{n1}{n2}-{n3}{n4}{n5}-{n6}{n7}{n8}'   

    def __init__(self, nimi, ika):
        """Luo asiakkaan tiedot.

        :param nimi: antaa nimen
        :type nimi: str
        :param _asiakasnro: antaa asiakas numeron
        :type _asiakasnro: int
        :param _ika: antaa iän
        :type _ika: int
        """
        self._nimi = nimi, str
        self._ika = ika, int
        self._asiakasnro = self._luo_nro()

    def get_nimi(self):
        try: 
            return print(self._nimi)
        except NameError:
            print("Suosittelen antamaan uuden nimen")

    def set_nimi(self, uusi_ika):
        self._nimi = uusi_ika

    def get_ika(self):
        try:
            return print(self._ika)
        except ValueError:
            print("Kehotan antamaan uuden nimen ja iän")

    def set_ika(self, ika):
        self._ika = ika

    def get_nro(self):
        return print(self._asiakasnro)

s = Asiakas('Tero', '15')
s.get_nimi()
s.set_nimi('Santeri')
s.get_nimi()
s.get_ika()
s.set_ika('51')
s.get_ika()
s.get_nro()


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
        :param _asiakasnro: antaa asiakas numeron
        :type _asiakasnro: int
        :param _asiakkaat: hakee asiakkaat
        :type _asiakkaat: Union[int, float]
        """
        self.tuotenimi = tuotenimi
        self._asiakkaat = Asiakas()

    def __luo_asiakasrivi(_asiakkaat):
        pass

    def lisaa_asiakas(_asiakkaat):
        try:
            _asiakkaat += '2'
        except ValueError:
            print("Anna asiakas")

    def tulosta_asiakkaat():
        pass

class ParempiPalvelu(Palvelu):
    """Luokka, mikä on parempi palvelu, kun normaali 
    
    Julkiset methodit:
        lisaa_etu(),
        poista_etu(),
        tulosta_edut()
    """
    def __init__(self, tuotenimi):
        """Ottaa edut tuotteesta

        :param _edut: asettaa edut tuotenimi listaksi
        :type _edut: str
        """
        self._edut = [tuotenimi]
    
    def lisaa_etu(edut):
        pass
    
    def poista_etu(edut):
        pass
    
    def tulosta_edut(edut):
        pass
