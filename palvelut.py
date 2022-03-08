class Asiakas():
    """Luokka, joka antaa asiakkaalle nimen, numeron, iän ja luo numeron
    
    Julkiset methodit:
    """
    def __init__(self):
        """Luo asiakkaan tiedot.

        :param nimi: antaa nimen
        :type nimi: str
        :param _asiakasnro: antaa asiakas numeron
        :type _asiakasnro: int
        :param _ika: antaa iän
        :type _ika: int
        """
        self._nimi = nimi
        self._asiakasnro = 1
        self._ika = ika
    def _luo_nro():
        pass

class Palvelu(Asiakas):
    """Luokka, millä voit muokata asiakkaita 
    
    Julkiset methodit:
        lisaa_asiakas(_asiakkaat)
        tulosta_asiakkaat()
    """
    def __init__(self):
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
    def __init__(self):
        self._edut = [str]
