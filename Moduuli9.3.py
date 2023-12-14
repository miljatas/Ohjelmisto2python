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
    uusi_auto = Auto(rekisteritunnus="ABC-123", huippunopeus=142)

    print("Luodun auton tiedot:")
    print(f"Rekisteritunnus: {uusi_auto.rekisteritunnus}")
    print(f"Huippunopeus: {uusi_auto.huippunopeus} km/h")
    print(f"Nykyinen nopeus: {uusi_auto.nykyinen_nopeus} km/h")
    print(f"Kuljettu matka: {uusi_auto.kuljettu_matka} km")

    # Kiihdytetään autoa
    uusi_auto.kiihdytä(30)
    print("\nAuton nopeus kiihdytyksen jälkeen: ", uusi_auto.nykyinen_nopeus, " km/h")

    uusi_auto.kiihdytä(70)
    print("Auton nopeus kiihdytyksen jälkeen: ", uusi_auto.nykyinen_nopeus, " km/h")

    uusi_auto.kiihdytä(50)
    print("Auton nopeus kiihdytyksen jälkeen: ", uusi_auto.nykyinen_nopeus, " km/h")

    # Hätäjarrutus
    uusi_auto.kiihdytä(-200)
    print("Auton nopeus hätäjarrutuksen jälkeen: ", uusi_auto.nykyinen_nopeus, " km/h")

    # Kuljetaan autoa ja päivitetään kuljettu matka
    uusi_auto.kulje(1.5)
    print("Kuljetun matkan lukema: ", uusi_auto.kuljettu_matka, " km")

if __name__ == "__main__":
    main()
