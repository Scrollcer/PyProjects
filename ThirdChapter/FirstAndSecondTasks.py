import random
# ----------------------------------------
# First task
# ----------------------------------------
value = random.randrange(4)
filling = ""
if value == 0:
    filling = "apples"
elif value == 1:
    filling = "bananas"
elif value == 2:
    filling = "apricots"
elif value == 3:
    filling = "plums"
elif value == 4:
    filling == "cabbage"
print("You got a hotcake with", filling)
# ----------------------------------------
# Second task
# ----------------------------------------
throw = 0
tails = 0
count = 0
eagles = 0

while count != 100:
    throw = random.randint(0, 1)
    if throw == 0:
        tails += 1
    else:
        eagles += 1
    count += 1
print("Tails count:", tails)
print("Eagle count:", eagles)
