# -----------------------------------------------------------------
# First task
# -----------------------------------------------------------------
firstDish = input("Please, enter your first favourite dish: ")
secondDish = input("Please, enter your second favourite dish: ")
print("You definitely should try", firstDish + secondDish)
# -----------------------------------------------------------------
# Second task
# -----------------------------------------------------------------
dinnerSum = int(input("Please, enter your dinner sum: "))
print("Tips values are", dinnerSum * 0.15, "or", dinnerSum * 0.2)
# -----------------------------------------------------------------
# Third task
# -----------------------------------------------------------------
priceAuto = int(input("Please, enter your car price: "))
finalPrice = priceAuto
finalPrice += priceAuto * 0.13
finalPrice += priceAuto * 0.20
finalPrice += 2000
print("Final car price will be:", finalPrice)
