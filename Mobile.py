# We do some oop exercise


class Mobile:

     Sim = True
     Ram = True
     Rom = True
     CircuitBoard = True

     def __init__(self, ram, sim, rom, color, displaySize):

                self.ram = ram
                self.sim = sim
                self.rom = rom
                self.color = color
                self.displaySize = displaySize


# mobile1 = Mobile("2Gb", "Banglalink", "16Gb", "Black", "6.5''")
# mobile2 = Mobile("1Gb", "GramaenPhone", "8Gb", "Black", "4.5''")
