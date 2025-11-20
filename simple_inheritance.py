class Animal:
    multicellular = True
    eukaryotic = True
    def breathe(self):
        print("I breathe oxygen")
class Herbivorous(Animal):
    def feed(self):
        print("I eat food")
herbi = Herbivorous()
herbi.feed()
herbi.breathe()