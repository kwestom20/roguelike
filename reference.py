#print("hello world")
# variable1= input("One or Two?")
# if variable1=="One":
#     print("One is the lonliest number")
# else: print("Two leads to Three and Three's a company")

# BASIC TYPES -----

# -- NUMBERS
my_integer = 5 # numbers can be whole numbers (integers)
my_float = 0.5 # they can also be decimal values (doubles or floats)

what_happens = my_integer + my_float # we're adding a float to an integer
print(what_happens) # guess what happens here?
# when adding decimals to integers, the result is a decimal

# -- STRINGS
my_string = "hello"
my_second_string = "world"
print(my_string + my_second_string) # concatenation means to join two strings
print(my_string, my_second_string) # print with multiple arguments will add a space by default
print(my_string, my_second_string, sep='') # you can tell it to not add a space
print(my_string, end='') # the "new line" after a print statement is actually it's own special, invisible character
print("hello\nworld") # you can manually add this special character '\n' in your text to force a new line
print("hello"*10) # you can repeat words with the '*' symbol

# ----- COMMON TYPES -----
my_list = [1,2,3,4,5,6,7,8,9] # you can change the values inside a list
my_tuple = (1, 2, 3, 4, 5) # you cannot change the values inside a tuple
# both are allowed to have multpile types of things in them
my_mixed_list = [1, "asdf", 2, "fdsa"]
my_mixed_tuple = (1, "asdf", 2, "fdsa")

print(my_list)
print(my_tuple)

my_list[1]=500
try:
    my_tuple[1]=500 # this will error. The try/except block prevents that error from crashing your program
except:
    print("you can't change a value inside a tuple")

print(my_list)
print(my_tuple)

# -- DICTIONARY
# dictionaries are key/value pairs that can be accessed and overwritten using the key
my_dict = {"favorite": "The Lion, the Witch, and the Wardrobe",
            "home": "Boise, ID",
            1: "One",
            2: "Two"}
print(my_dict)
print(my_dict["favorite"])
print(my_dict[1])
my_dict[2] = "not two anymore, HAH" # you can overwrite keys
print(my_dict[2])
my_dict[3] = "Three's a crowd"
print(my_dict[3]) # you can add new keys and values

print("--- dictionary keys ---")
for k in my_dict.keys():
    print(k) # you can iterate over the keys themselves as a list

print("--- dictionary values ---")
for v in my_dict.values():
    print(v) # you can iterate over the values too

# ----- COMPLEX TYPES -----
class Dog:
    leg_count=4
    size="large"
    def bark(self):
        print("Barking!")

class Mixed(Dog):
    def bark(self):
        print("Mixed Barking!")
class Medium(Dog):
    size="medium"
class Custom(Dog):
    def __init__(self, legs, size):
        self.size=legs
        self.size=size
class Modular(Dog):
    def __init__(self, legs=None, size=None):
        if legs is not None: # if statement to find out if None
            self.leg_count = legs
        else:
            self.leg_count = super().legs # super() gets the parent object (Dog in this case)

        self.size = size if size else super().size # ternary operator to do the same thing

rando=Dog()
sammy=Mixed()
medium=Medium()
modular=Modular(legs=3)
sammy.size="medium"

print("Rando: Legs:", rando.leg_count)
print("Sammy: Legs:", sammy.leg_count)
print("Modular: Legs:", modular.leg_count)

print("Rando: Size:", rando.size)
print("Sammy: Size:", sammy.size)
print("Medium: Size:", medium.size)

rando.bark()
sammy.bark()