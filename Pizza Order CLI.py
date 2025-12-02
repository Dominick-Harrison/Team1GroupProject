print("Hello, welcome to nondescript pizza terminal!")

# initialize vars
size_prices = {
        "S": 15,
        "M": 20,
        "L": 25
    }
total = 0
valid_size = False
valid_pepperoni = False
valid_cheese = False

# start a loop and prompt user for their pizza size, stores answer in "size"
while not valid_size:
    size = input("Choose a size (S/M/L): ").strip().upper()
    if size in size_prices:
         valid_size = True
    else:
        print("Invalid size entered. Please enter S, M, or L.")
    
total = size_prices[size]

# prompt for pepperoni, then add to final bill
while not valid_pepperoni:
    pepperoni = input("Add pepperoni? (Y/N): ").strip().upper()
# validate pepperoni input
    if pepperoni in ["Y", "N"]:
        valid_pepperoni = True
    else:
        print("Please enter Y or N.")
if pepperoni == "Y":
    if size == "S":
        total += 2
    else:
        total += 3

# prompt for cheese, then adjust final bill
while not valid_cheese:
    cheese = input("Add extra cheese? (Y/N): ").strip().upper()
# validate cheese input
    if cheese in ["Y", "N"]:
        valid_cheese = True
    else:
        print("Please enter Y or N.")
if cheese == "Y":
    total += 1

print(f"Your final bill is: ${total}")
print("Thank you for ordering from nondescript pizza terminal!")

input("\nPress Enter to exit...")