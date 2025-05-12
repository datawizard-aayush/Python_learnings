# If= Do some code only IF some condition is True
# Else do something else
# the order of if else statements matters a lot otherwise the first one will get executed
# without checking the second condition for e.g.age>=100 and age>=18 has to be correct order.

    #Printing name correctly program
import string
while True:
    name = input("Enter your name: ").strip()  # Remove leading and trailing spaces
    if name == "":
      print("Please enter a correct name.")
    elif any(char in string.punctuation for char in name):  # Check for special characters
         print("Name should not include special characters. \t Try again....") #\t gives a spacing between 2 lines
    elif any(char.isdigit() for char in name):  # Check for numbers
         print("Name should not include numbers.\t\tTry again....")
    else:
        print(f"Hello, {name}!")
        break
#Boolean if-else
for_sale=True
if for_sale:
    print("\nItem is for sale")
else:
    print("\nItem is not for sale")
