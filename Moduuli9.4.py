import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        uusi_nopeus = self.nykyinen_nopeus + nopeuden_muutos
        self.nykyinen_nopeus = min(uusi_nopeus, self.huippunopeus)
        self.nykyinen_nopeus = max(self.nykyinen_nopeus, 0)

    def kulje(self, tuntimäärä):
        matka = self.nykyinen_nopeus * tuntimäärä
        self.kuljettu_matka += matka

# Pääohjelma
def main():
    autot = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        uusi_auto = Auto(rekisteritunnus, huippunopeus)
        autot.append(uusi_auto)

    kilpailu_jatkuu = True
    tunti = 1

    while kilpailu_jatkuu:
        print(f"\nTunti {tunti}:\n")
        for auto in autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)

            print(f"Auto {auto.rekisteritunnus}: Nopeus - {auto.nykyinen_nopeus} km/h, Kuljettu matka - {auto.kuljettu_matka} km")

            if auto.kuljettu_matka >= 10000:
                kilpailu_jatkuu = False

        tunti += 1

    print("\nKilpailun tulokset:\n")
    print("Rekisteritunnus | Huippunopeus | Viimeisin nopeus | Kuljettu matka")
    print("---------------------------------------------------------------")
    for auto in autot:
        print(f"{auto.rekisteritunnus}        | {auto.huippunopeus} km/h         | {auto.nykyinen_nopeus} km/h              | {auto.kuljettu_matka} km")

if __name__ == "__main__":
    main()
