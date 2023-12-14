class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

# Pääohjelma
def main():
    uusi_auto = Auto(rekisteritunnus="ABC-123", huippunopeus=142)

    print("Luodun auton tiedot:")
    print(f"Rekisteritunnus: {uusi_auto.rekisteritunnus}")
    print(f"Huippunopeus: {uusi_auto.huippunopeus} km/h")
    print(f"Nykyinen nopeus: {uusi_auto.nykyinen_nopeus} km/h")
    print(f"Kuljettu matka: {uusi_auto.kuljettu_matka} km")

if __name__ == "__main__":
    main()