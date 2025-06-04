from datetime import date

class Llama:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Donkey:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Goat:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Sheep:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Pig:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

# Glass Tank Animals
class Copperhead:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class RatSnake:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class CornSnake:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class Gecko:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class Iguana:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

# Pond Animals
class Mallard:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Goldfish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Koi:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Turtle:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Frog:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

# Instances
miss_fuzz = Llama("Miss Fuzz", "domestic llama")
mr_shrek = Donkey("Mr. Shrek", "domestic donkey")
tiger_woods = Goat("Tiger Woods", "pygmy goat")
wooly_nelson = Sheep("Wooly Nelson", "merino sheep")
ham_solo = Pig("Ham Solo", "pot-bellied pig")

danger_noodle = Copperhead("Danger Noodle", "copperhead snake")
mr_slinky = RatSnake("Mr. Slinky", "rat snake")
spaghetti = CornSnake("Spaghetti", "corn snake")
leon = Gecko("Leon", "leopard gecko")
iguana_jones = Iguana("Iguana Jones", "green iguana")

quackmire = Mallard("Quackmire", "mallard duck")
gill_bates = Goldfish("Gill Bates", "goldfish")
wavey = Koi("Wavey", "koi carp")
slowpoke = Turtle("Slowpoke", "red-eared slider")
ribbit_downey_jr = Frog("Ribbit Downey Jr.", "bullfrog")

animals = [
    miss_fuzz, mr_shrek, tiger_woods, wooly_nelson, ham_solo,
    danger_noodle, mr_slinky, spaghetti, leon, iguana_jones,
    quackmire, gill_bates, wavey, slowpoke, ribbit_downey_jr
]

for animal in animals:
    print(f"{animal.name} the {animal.species} was added on {animal.date_added}.")

print(miss_fuzz)