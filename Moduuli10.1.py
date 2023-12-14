class Hissi:
    def __init__(self, alin_kerros, ylimmäinen_kerros):
        self.kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylimmäinen_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin_kerros or kohde_kerros > self.ylin_kerros:
            print("Virhe: Kohdekerros ei ole hissin liikkumisalueella.")
            return

        while self.kerros != kohde_kerros:
            if self.kerros < kohde_kerros:
                self.kerros_ylös()
            else:
                self.kerros_alas()

    def kerros_ylös(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
            print(f"Hissi siirtyi kerrokseen {self.kerros}")
        else:
            print("Hissi on jo ylimmäisessä kerroksessa.")

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
            print(f"Hissi siirtyi kerrokseen {self.kerros}")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

# Testaa luokkaa
if __name__ == "__main__":
    hissi = Hissi(alin_kerros=1, ylimmäinen_kerros=10)

    print("Hissi alkaa alimmasta kerroksesta.")
    hissi.siirry_kerrokseen(5)

    print("\nHissi palaa alimpaan kerrokseen.")
    hissi.siirry_kerrokseen(1)
