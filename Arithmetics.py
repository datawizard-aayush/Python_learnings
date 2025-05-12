#define a variable x to be zero
x=10
x = x+1 #we can also use x+=1 (to take less time called augmented)
print(x)
x -= 2   #x=x-2 Subtraction
print(x)
x *= 3   #x=x*3 Multiplication
print(x)
def convert_if_int(number):
    if number.is_integer():  # Check if it's essentially an integer (i.e., has .0)
        return int(number)  # Convert to int if .0
    return number  # Otherwise return the number as is
x /= 2   #x=x/2 Division
x=convert_if_int(x)
print(x)
x **= 2  #x=x**2 Power
x = convert_if_int(x)
print(x)
x//=2 #x=x//2 Floor division
print(f"Before convert int {x}")
x = convert_if_int(x)
print(f"After convert int {x}")
remainder=x%3 #modulus
x = convert_if_int(x)
print(remainder)
