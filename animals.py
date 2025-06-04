from datetime import date

class Llama:
    def  __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

class Donkey:
    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

class Goat:
    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

class Sheep:
    def __init__(self):
        self.name = ""
        self.species = "merino sheep"
        self.date_added = date.today()
        self.walking = True

class Pig:
    def __init__(self):
        self.name = ""
        self.species = "pot-bellied pig"
        self.date_added = date.today()
        self.walking = True

# Glass Tank Animals
class Copperhead:
    def __init__(self):
        self.name = ""
        self.species = "copperhead snake"
        self.date_added = date.today()
        self.slithering = True

class RatSnake:
    def __init__(self):
        self.name = ""
        self.species = "rat snake"
        self.date_added = date.today()
        self.slithering = True

class CornSnake:
    def __init__(self):
        self.name = ""
        self.species = "corn snake"
        self.date_added = date.today()
        self.slithering = True

class Gecko:
    def __init__(self):
        self.name = ""
        self.species = "leopard gecko"
        self.date_added = date.today()
        self.slithering = True

class Iguana:
    def __init__(self):
        self.name = ""
        self.species = "green iguana"
        self.date_added = date.today()
        self.slithering = True

# Pond Animals
class Mallard:
    def __init__(self):
        self.name = ""
        self.species = "mallard duck"
        self.date_added = date.today()
        self.swimming = True

class Goldfish:
    def __init__(self):
        self.name = ""
        self.species = "goldfish"
        self.date_added = date.today()
        self.swimming = True

class Koi:
    def __init__(self):
        self.name = ""
        self.species = "koi carp"
        self.date_added = date.today()
        self.swimming = True

class Turtle:
    def __init__(self):
        self.name = ""
        self.species = "red-eared slider"
        self.date_added = date.today()
        self.swimming = True

class Frog:
    def __init__(self):
        self.name = ""
        self.species = "bullfrog"
        self.date_added = date.today()
        self.swimming = True

miss_fuzz = Llama()
miss_fuzz.name = "Miss Fuzz"
miss_fuzz.species = "domestic llama"
miss_fuzz.date_added = date.today()

mr_shrek = Donkey()
mr_shrek.name = "mr shrek"
mr_shrek.species = "domestic donkey"
mr_shrek.date_added = date.today()
mr_shrek.walking = True

tiger_woods = Goat()
tiger_woods.name = "tiger woods"
tiger_woods.species = "pygmy goat"
tiger_woods.date_added = date.today()
tiger_woods.walking = True

wooly_nelson = Sheep()
wooly_nelson.name = "Wooly Nelson"
wooly_nelson.species = "merino sheep"
wooly_nelson.date_added = date.today()
wooly_nelson.walking = True

ham_solo = Pig()
ham_solo.name = "Ham Solo"
ham_solo.species = "pot-bellied pig"
ham_solo.date_added = date.today()
ham_solo.walking = True

# Glass tank
danger_noodle = Copperhead()
danger_noodle.name = "Danger Noodle"
danger_noodle.species = "copperhead snake"
danger_noodle.date_added = date.today()
danger_noodle.slithering = True

mr_slinky = RatSnake()
mr_slinky.name = "Mr. Slinky"
mr_slinky.species = "rat snake"
mr_slinky.date_added = date.today()
mr_slinky.slithering = True

spaghetti = CornSnake()
spaghetti.name = "Spaghetti"
spaghetti.species = "corn snake"
spaghetti.date_added = date.today()
spaghetti.slithering = True

leon = Gecko()
leon.name = "Leon"
leon.species = "leopard gecko"
leon.date_added = date.today()
leon.slithering = True

iguana_jones = Iguana()
iguana_jones.name = "Iguana Jones"
iguana_jones.species = "green iguana"
iguana_jones.date_added = date.today()
iguana_jones.slithering = True

# Pond
quackmire = Mallard()
quackmire.name = "Quackmire"
quackmire.species = "mallard duck"
quackmire.date_added = date.today()
quackmire.swimming = True

gill_bates = Goldfish()
gill_bates.name = "Gill Bates"
gill_bates.species = "goldfish"
gill_bates.date_added = date.today()
gill_bates.swimming = True

wavey = Koi()
wavey.name = "Wavey"
wavey.species = "koi carp"
wavey.date_added = date.today()
wavey.swimming = True

slowpoke = Turtle()
slowpoke.name = "Slowpoke"
slowpoke.species = "red-eared slider"
slowpoke.date_added = date.today()
slowpoke.swimming = True

ribbit_downey_jr = Frog()
ribbit_downey_jr.name = "Ribbit Downey Jr."
ribbit_downey_jr.species = "bullfrog"
ribbit_downey_jr.date_added = date.today()
ribbit_downey_jr.swimming = True

animals = [
    miss_fuzz, mr_shrek, tiger_woods, wooly_nelson, ham_solo,
    danger_noodle, mr_slinky, spaghetti, leon, iguana_jones,
    quackmire, gill_bates, wavey, slowpoke, ribbit_downey_jr
]

for animal in animals:
    print(f"{animal.name} the {animal.species} was added on {animal.date_added}.")

print(miss_fuzz)