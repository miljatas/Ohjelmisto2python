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


class Talo:
    def __init__(self, alin_kerros, ylimmäinen_kerros, hissien_lukumäärä):
        self.hissit = [Hissi(alin_kerros, ylimmäinen_kerros) for _ in range(hissien_lukumäärä)]

    def aja_hissiä(self, hissi_numero, kohde_kerros):
        if hissi_numero < 1 or hissi_numero > len(self.hissit):
            print("Virhe: Hissinumero ei ole talon hissien lukumäärän rajoissa.")
            return

        hissi = self.hissit[hissi_numero - 1]
        print(f"\nAjetaan hissiä {hissi_numero} kohteeseen {kohde_kerros}")
        hissi.siirry_kerrokseen(kohde_kerros)

    def palohälytys(self):
        print("\nPalohälytys! Kaikki hissit siirtyvät pohjakerrokseen.")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.hissit[0].alin_kerros)


# Pääohjelma
if __name__ == "__main__":
    talo = Talo(alin_kerros=1, ylimmäinen_kerros=10, hissien_lukumäärä=2)

    # Aja ensimmäinen hissi kerrokseen 5
    talo.aja_hissiä(1, 5)

    # Aja toinen hissi kerrokseen 8
    talo.aja_hissiä(2, 8)

    # Simuloi palohälytys
    talo.palohälytys()
