from datetime import date

from walking import Llama, Donkey, Goat, Sheep, Pig
from slithering import Copperhead, RatSnake, CornSnake, Gecko, Iguana
from swimming import Mallard, Goldfish, Koi, Turtle, Frog

# Instances
miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow")
print(f"{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {miss_fuzz.shift}.")
print(miss_fuzz)
miss_fuzz.feed()

mr_shrek = Donkey("Mr. Shrek", "domestic donkey", "midday", "Donkey chow")
print(f"{mr_shrek.name} the {mr_shrek.species} is available to pet during the {mr_shrek.shift}.")
print(mr_shrek)
mr_shrek.feed()

tiger_woods = Goat("Tiger Woods", "pygmy goat", "afternoon", "Goat Feed")
print(f"{tiger_woods.name} the {tiger_woods.species} is available to pet during the {tiger_woods.shift}.")
print(tiger_woods)
tiger_woods.feed()

wooly_nelson = Sheep("Wooly Nelson", "merino sheep", "morning", "Sheep Feed")
print(f"{wooly_nelson.name} the {wooly_nelson.species} is available to pet during the {wooly_nelson.shift}.")
print(wooly_nelson)
wooly_nelson.feed()

ham_solo = Pig("Ham Solo", "pot-bellied pig", "midday", "Slop")
print(f"{ham_solo.name} the {ham_solo.species} is available to pet during the {ham_solo.shift}.")
print(ham_solo)
ham_solo.feed()

danger_noodle = Copperhead("Danger Noodle", "copperhead snake", "Live Feed")
print(danger_noodle)
danger_noodle.feed()

mr_slinky = RatSnake("Mr. Slinky", "rat snake", "Live Feed")
print(mr_slinky)
mr_slinky.feed()

spaghetti = CornSnake("Spaghetti", "corn snake", "Live Feed")
print(spaghetti)
spaghetti.feed()

leon = Gecko("Leon", "leopard gecko", "Live Feed")
print(leon)
leon.feed()

iguana_jones = Iguana("Iguana Jones", "green iguana", "Live Feed")
print(iguana_jones)
iguana_jones.feed()

quackmire = Mallard("Quackmire", "mallard duck", "Live Feed")
print(quackmire)
quackmire.feed()

gill_bates = Goldfish("Gill Bates", "goldfish", "Fish Feed")
print(gill_bates)
gill_bates.feed()

wavey = Koi("Wavey", "koi carp", "Fish Feed")
print(wavey)
wavey.feed()

slowpoke = Turtle("Slowpoke", "red-eared slider", "Fish Feed")
print(slowpoke)
slowpoke.feed()

ribbit_downey_jr = Frog("Ribbit Downey Jr.", "bullfrog", "Live Bugs")
print(ribbit_downey_jr)
ribbit_downey_jr.feed()

#Sample Output 
# animals = [
#     miss_fuzz, mr_shrek, tiger_woods, wooly_nelson, ham_solo,
#     danger_noodle, mr_slinky, spaghetti, leon, iguana_jones,
#     quackmire, gill_bates, wavey, slowpoke, ribbit_downey_jr
# ]

# for animal in animals:
#     print(f"{animal.name} the {animal.species} was added on {animal.date_added}.")
