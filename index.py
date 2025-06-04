from datetime import date

from walking import Llama, Donkey, Goat, Sheep, Pig
from slithering import Copperhead, RatSnake, CornSnake, Gecko, Iguana
from swimming import Mallard, Goldfish, Koi, Turtle, Frog

# Instances
miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow")
print(f"{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {miss_fuzz.shift}.")
miss_fuzz.feed()

mr_shrek = Donkey("Mr. Shrek", "domestic donkey", "midday", "Donkey chow")
print(f"{mr_shrek.name} the {mr_shrek.species} is available to pet during the {mr_shrek.shift}.")
mr_shrek.feed()

tiger_woods = Goat("Tiger Woods", "pygmy goat", "afternoon", "Goat Feed")
print(f"{tiger_woods.name} the {tiger_woods.species} is available to pet during the {tiger_woods.shift}.")
tiger_woods.feed()

wooly_nelson = Sheep("Wooly Nelson", "merino sheep", "morning", "Sheep Feed")
print(f"{wooly_nelson.name} the {wooly_nelson.species} is available to pet during the {wooly_nelson.shift}.")
wooly_nelson.feed()

ham_solo = Pig("Ham Solo", "pot-bellied pig", "midday", "Slop")
print(f"{ham_solo.name} the {ham_solo.species} is available to pet during the {ham_solo.shift}.")
ham_solo.feed()

danger_noodle = Copperhead("Danger Noodle", "copperhead snake", "Live Feed")
danger_noodle.feed()

mr_slinky = RatSnake("Mr. Slinky", "rat snake", "Live Feed")
mr_slinky.feed()

spaghetti = CornSnake("Spaghetti", "corn snake", "Live Feed")
spaghetti.feed()

leon = Gecko("Leon", "leopard gecko", "Live Feed")
leon.feed()

iguana_jones = Iguana("Iguana Jones", "green iguana", "Live Feed")
iguana_jones.feed()

quackmire = Mallard("Quackmire", "mallard duck", "Live Feed")
quackmire.feed()

gill_bates = Goldfish("Gill Bates", "goldfish", "Fish Feed")
gill_bates.feed()

wavey = Koi("Wavey", "koi carp", "Fish Feed")
wavey.feed()

slowpoke = Turtle("Slowpoke", "red-eared slider", "Fish Feed")
slowpoke.feed()

ribbit_downey_jr = Frog("Ribbit Downey Jr.", "bullfrog", "Live Bugs")
ribbit_downey_jr.feed()

#Sample Output 
# animals = [
#     miss_fuzz, mr_shrek, tiger_woods, wooly_nelson, ham_solo,
#     danger_noodle, mr_slinky, spaghetti, leon, iguana_jones,
#     quackmire, gill_bates, wavey, slowpoke, ribbit_downey_jr
# ]

# for animal in animals:
#     print(f"{animal.name} the {animal.species} was added on {animal.date_added}.")
