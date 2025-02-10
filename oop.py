import random 

class Character:
    #class attributes
    hair_colors = ["Blonde", "Brown", "Black", "Red"]
    sizes = ["Tiny", "Medium", "Large"]
    special_powers = ["Flying", "Teleportation", "Invisibility", "Super Strength", "Mind Reading"]

    #Constructor
    def __init__(self):
        self.generate_character()

#This is a method (function)
def generate_character(self):
    self.hair_color = random.choice(Character.hair_colors)
    self.size = random.choice(Character.sizes)
    self.special_power = random.choice(Character.special_powers)
    self.description = (
        f"Your Character has {self.hair_color} hair, "
        f"is {self.size} on size, "
        f"and has the power of {self.special_power}"
    )

def ___str___(self):
    return self.description 

char1 = Character()
char2 = Character()

print(char1)
print(char2)