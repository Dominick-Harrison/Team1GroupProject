print("Hello, welcome to nondescript pizza terminal!")

# initialize vars
SIZE_PRICES = {
        "S": 15,
        "M": 20,
        "L": 25
    }
totalPrice = 0
validSize = False
validPepperoni = False
validCheese = False

# start a loop and prompt user for their pizza size, stores answer in "size"
while not validSize:
    chooseSize = input("Choose a size (S/M/L): ").strip().upper()
    if chooseSize in SIZE_PRICES:
         validSize = True
    else:
        print("Invalid size entered. Please enter S, M, or L.")
    
totalPrice = SIZE_PRICES[chooseSize]

# prompt for pepperoni, then add to final bill
while not validPepperoni:
    pepperoniAdd = input("Add pepperoni? (Y/N): ").strip().upper()
# validate pepperoni input
    if pepperoniAdd in ["Y", "N"]:
        validPepperoni = True
    else:
        print("Please enter Y or N.")
if pepperoniAdd == "Y":
    if chooseSize == "S":
        totalPrice += 2
    else:
        totalPrice += 3

# prompt for cheese, then adjust final bill
while not validCheese:
    cheeseAdd = input("Add extra cheese? (Y/N): ").strip().upper()
# validate cheese input
    if cheeseAdd in ["Y", "N"]:
        validCheese = True
    else:
        print("Please enter Y or N.")
if cheeseAdd == "Y":
    totalPrice += 1

print(f"Your final bill is: ${totalPrice}")
print("Thank you for ordering from nondescript pizza terminal!")

input("\nPress Enter to exit...")
