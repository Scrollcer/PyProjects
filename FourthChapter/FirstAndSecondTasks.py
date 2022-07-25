# ----------------------------------------------------------------------
# First task
# ----------------------------------------------------------------------
first = int(input("Please, enter first number: "))
second = int(input("Enter second number: "))
interval = int(input("Enter range: "))
for i in range(first, second, interval):
    print(i)
# ----------------------------------------------------------------------
# Second task
# ----------------------------------------------------------------------
reverse = ""
text = input("Please, enter text to reverse: ")
for i in text:
    reverse = i + reverse
print(reverse)
