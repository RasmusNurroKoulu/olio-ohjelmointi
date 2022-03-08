class Asiakas:
    """Luokka, joka antaa asiakkaalle nimen, numeron, iän ja luo numeron
    
    Julkiset methodit:
    """
    def __init__(self, nimi, ika):
        """Luo asiakkaan tiedot.

        :param nimi: antaa nimen
        :type nimi: str
        :param _asiakasnro: antaa asiakas numeron
        :type _asiakasnro: int
        :param _ika: antaa iän
        :type _ika: int
        """
        self._nimi = nimi
        self._ika = ika
        self._asiakasnro = 2

    def get_nimi(self):
        try: 
            self._nimi
        except NameError:
            print("Suosittelen antamaan uuden nimen")

    def set_nimi(self, uusi_ika):
        self._nimi = uusi_ika

    def get_ika(self):
        try:
            return self._ika
        except ValueError:
            print("Kehotan antamaan uuden nimen ja iän")

    def set_ika(self, ika):
        self._ika = ika


    def _luo_nro():
        pass

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
        pass

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
