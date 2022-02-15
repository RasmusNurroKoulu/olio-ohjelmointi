import random
import time

class Olento:
     def __init__(self, nimi, pohjarohkeus=1, pohjakatse=1):
        """Perintä luokka, joka toimii pohjana
        :ivar nimi: nimi annetaan
        :type nimi: str
        :ivar rouhkeus: olentojen rohkeus, joka arvotaan
        :type rohkeus: int
        :ivar katseen_voima: olenojen katseen voimakkuus, joka arvotaan
        :ivar katseen_voima: int"""
        self.nimi = nimi
        self.rohkeus = random.randint(pohjarohkeus, pohjarohkeus + 3)
        self.katseen_voima = random.randint(pohjakatse, pohjakatse + 3)
     def arvo_hurraus(self):
        pass

class Peikko(Olento):

    """Luokka, joka kuvaa Peikon.
    :ivar nimi: peikon nimi, arvotaan
    :type nimi: str
    :ivar rohkeus: peikon rohkeus, arvotaan
    :type rohkeus: int
    :ivar katseen_voima: peikon katseen voimakkuus, arvotaan
    :type katseen_voima: int

    Julkiset metodit
        arvo_hurraus()
    """

    NIMITAVUT = ("Ur", "Gar", "Grah", "Gur", "Kan", "Kazah", "Bar", "Bazh", "Ragh", "Rudz")
    RIEMUTAVUT = ("Agh", "Ugh", "Ourgh", "Drar", "Brar", "Dza", "Gra", "Gur", "Rah", "Urgh", "Ra")

    def __init__(self, pohjarohkeus = 1, pohjakatse = 2):
        """Konstruktori."""
        nimi = self._arvo_sanat(self.NIMITAVUT, 3, "-")
        super().__init__(nimi, pohjarohkeus, pohjakatse)

    def _arvo_sanat(self, tavut, n, erotin, p=0.5):
        """Muodostaa satunnaisen tekstin annetuista tavuista.

        :param tavut: ne tavut, joita palautettava teksti voi sisältää
        :type tavut: Union[list[str], tuple[str]]
        :param n: mukaan poimittavien tavujen maksimimäärä
        :type n: int
        :param erotin: tavujen väliin satunnaisesti laitettava merkki
        :type erotin: str
        :param p: todennäköisyys lisätä erotin tavujen väliin (oletus 0.5)
        :type p: float
        :return: satunnainen teksti
        :rtype: str
        """
        osat = random.choices(tavut, k=random.randint(2, n))
        sanat = osat[0]
        for osa in osat[1:]:
            if random.random() < p:
                sanat += erotin + osa
            else:
                sanat += osa.lower()
        return sanat

    def arvo_hurraus(self):
        """Palauttaa satunnaisen hurraushuudahduksen.

        :return: hurraava huudahdus
        :rtype: str
        """
        return self._arvo_sanat(self.RIEMUTAVUT, 8, " ", 0.7)

class Vuorenpeikko(Peikko):
    """:ivar NIMITAVUT2: nimitavut
    :type NIMITAVUT2: str
    :ivar RIEMUTAVUT2: nimitavut
    :type RIEMUTAVUT2: str
    """
    NIMITAVUT = ("Puh", "Pah", "Pew", "Pow", "Por", "Pot", "Pos", "Pob", "Pub", "Pab")
    RIEMUTAVUT = ("Argh", "Orgh", "Urgh", "Ergh", "Irgh", "Arg", "Org", "Urg", "Erg", "Irg", "Rn")
    def __init__(self, pohjarohkeus = 1, pohjakatse = 4):
        super().__init__(pohjarohkeus, pohjakatse)

class Luolapeikko(Peikko):
    """:ivar NIMITAVUT1: nimitavut
    :type NIMITAVUT1: str
    :ivar RIEMUTAVUT1: nimitavut
    :type RIEMUTAVUT1: str
    """
    NIMITAVUT = ("Wuh", "Wah", "Weh", "Woh", "Wor", "Wot", "Wos", "Wob", "Wub", "Wab")
    RIEMUTAVUT = ("Arrgh", "Orrgh", "Urrgh", "Errgh", "Irrgh", "Arrg", "Orrg", "Urrg", "Errg", "Irrg", "Rrn")
    def __init__(self, pohjarohkeus = 5, pohjakatse = 2):
        super().__init__(pohjarohkeus, pohjakatse)

### Kirjoita luokka Sankari tähän.
class Sankari(Olento):
    """:ivar nimi: sankarin nimi, arvotaan
    :type nimi: str
    :ivar rohkeus: sankarin rohkeus, arvotaan
    :type rohkeus: int
    :ivar katseen_voima: sankarin katseen voimakkuus, arvotaan
    :type katseen_voima: int
    """
    def __init__(self, nimi, pohjarohkeus = 5, pohjakatse = 3):
        super().__init__(nimi, pohjarohkeus, pohjakatse)


    def arvo_hurraus(self):
        """Palauttaa satunnaisen hurraushuudahduksen.
        :type ARVOSATUNNAINEN: str
        :ivar ARVOSATUNNAINEN: lista hurrauduksista
        :return: hurraava huudahdus
        :rtype: str
        """
        ARVOSATUNAINEN = ["woo", "jee", "wohoo", "mennään", "jippii", "Yoooo"]
        return random.choice(ARVOSATUNAINEN)


def hurraa(olio):
    """Tulostaa satunnaisen hurrauksen annetulle oliolle.

    :param olio: hurraava olio
    """
    print('%s: "%s!"' % (olio.nimi, olio.arvo_hurraus()))


def tulosta_rapaytys(rapayttaja):
    """Tulostaa sopivan tekstin räpäyttävälle oliolle.

    :param rapayttaja: silmiään räpäyttävä olio
    """
    if rapayttaja:
        if rapayttaja.rohkeus > 0:
            print("ja %s räpäyttää!" % rapayttaja.nimi)
        else:
            print("ja %s karkaa!" % rapayttaja.nimi)
    else:
        print("eikä kummankaan silmä rävähdä!")


def tuijota(olio1, olio2):
    """Asettaa annetut oliot taistelemaan keskenään yhden kierroksen.

    :param vasen: ensimmäinen taisteleva olio
    :type vasen: Union[Sankari, Peikko]
    :param oikea: toinen taisteleva olio
    :type oikea: Union[Sankari, Peikko]
    :return: hävinnyt olio
    :rtype: Union[Sankari, Peikko]
    """
    print("He tuijottavat toisiaan...", end='')
    time.sleep(1)
    # Arvotaan kummankin olion tämän kierroksen vahvuus.
    katse1 = random.randint(0, olio1.katseen_voima)
    katse2 = random.randint(0, olio2.katseen_voima)
    rapayttaja = None

    # heikomman vahvuuden saanut olio menettää rohkeutta
    if katse1 > katse2:
        rapayttaja = olio2
        rapayttaja.rohkeus -= katse1
    elif katse1 < katse2:
        rapayttaja = olio1
        rapayttaja.rohkeus -= katse2
    return rapayttaja


def taistele(vasen, oikea):
    """Asettaa annetut oliot taistelemaan keskenään, kunnes toinen voittaa.

    :param vasen: ensimmäinen taisteleva olio
    :type vasen: Union[Sankari, Peikko]
    :param oikea: toinen taisteleva olio
    :type oikea: Union[Sankari, Peikko]
    :return: voittanut olio
    :rtype: Union[Sankari, Peikko]
    """
    while vasen.rohkeus > 0 and oikea.rohkeus > 0:
        haviaja = tuijota(vasen, oikea)
        tulosta_rapaytys(haviaja)
        time.sleep(0.5)
    if vasen.rohkeus > 0:
        return vasen
    else:
        return oikea


sankari = Sankari(input("Mikä on sankarimme nimi? "))
pelastetut = 0
# Käydään tuijotuskisoja peikkoja vastaan, kunnes sankari karkaa
while sankari.rohkeus > 0:
    # Tulostetaan kierroksen alkutiedot.
    sankarin_tiedot = sankari.nimi + " [" + str(sankari.rohkeus) + "]"
    print("Sankarimme %s kävelee kohti seikkailua." % sankarin_tiedot)
    time.sleep(0.7)

    # Tulostetaan vastaan tulevan peikon tiedot.
    peikko = random.choice([Peikko(), Vuorenpeikko(), Luolapeikko()])
    peikon_tiedot = peikko.nimi + " [" + str(peikko.rohkeus) + "]"
    print("Vastaan tulee hurja %s!" % peikon_tiedot)
    time.sleep(1)

    # Käydään tuijotuskisa peikkoa vastaan.
    voittaja = taistele(peikko, sankari)
    hurraa(voittaja)
    print()
    time.sleep(1.5)

time.sleep(1.5)
print("%s herää sängystään hikisenä - onneksi se oli vain unta!" % sankari.nimi)
