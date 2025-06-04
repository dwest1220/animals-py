from datetime import date

from walking import Llama, Donkey, Goat, Sheep, Pig
from slithering import Copperhead, RatSnake, CornSnake, Gecko, Iguana
from swimming import Mallard, Goldfish, Koi, Turtle, Frog

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

#Sample Output 
animals = [
    miss_fuzz, mr_shrek, tiger_woods, wooly_nelson, ham_solo,
    danger_noodle, mr_slinky, spaghetti, leon, iguana_jones,
    quackmire, gill_bates, wavey, slowpoke, ribbit_downey_jr
]

for animal in animals:
    print(f"{animal.name} the {animal.species} was added on {animal.date_added}.")
