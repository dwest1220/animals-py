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
    def __init__(self, name, species="merino sheep"):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Pig:
    def __init__(self, name, species="pot-bellied pig"):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

# Glass Tank Animals
class Copperhead:
    def __init__(self, name, species="copperhead snake"):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class RatSnake:
    def __init__(self, name, species="rat snake"):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class CornSnake:
    def __init__(self, name, species="corn snake"):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class Gecko:
    def __init__(self, name, species="leopard gecko"):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class Iguana:
    def __init__(self, name, species="green iguana"):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

# Pond Animals
class Mallard:
    def __init__(self, name, species="mallard duck"):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Goldfish:
    def __init__(self, name, species="goldfish"):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Koi:
    def __init__(self, name, species="koi carp"):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Turtle:
    def __init__(self, name, species="red-eared slider"):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Frog:
    def __init__(self, name, species="bullfrog"):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

miss_fuzz = Llama("Miss Fuzz", "domestic llama")
mr_shrek = Donkey("mr shrek", "domestic donkey")
tiger_woods = Goat("tiger woods", "pygmy goat")
wooly_nelson = Sheep("Wooly Nelson")
ham_solo = Pig("Ham Solo")

danger_noodle = Copperhead("Danger Noodle")
mr_slinky = RatSnake("Mr. Slinky")
spaghetti = CornSnake("Spaghetti")
leon = Gecko("Leon")
iguana_jones = Iguana("Iguana Jones")

quackmire = Mallard("Quackmire")
gill_bates = Goldfish("Gill Bates")
wavey = Koi("Wavey")
slowpoke = Turtle("Slowpoke")
ribbit_downey_jr = Frog("Ribbit Downey Jr.")

animals = [
    miss_fuzz, mr_shrek, tiger_woods, wooly_nelson, ham_solo,
    danger_noodle, mr_slinky, spaghetti, leon, iguana_jones,
    quackmire, gill_bates, wavey, slowpoke, ribbit_downey_jr
]

for animal in animals:
    print(f"{animal.name} the {animal.species} was added on {animal.date_added}.")

print(miss_fuzz)