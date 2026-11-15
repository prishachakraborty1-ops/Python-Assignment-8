class Animal:

    def __init__(self, type):
        self.type = type


class WildAnimal(Animal):

    def __init__(self, type, sound, color):
        super().__init__(type)
        self.sound = sound
        self.color = color

    def show(self):
        print("Wild Animal")
        print("Type:", self.type)
        print("Sound:", self.sound)
        print("Color:", self.color)


class PetAnimal(Animal):

    def __init__(self, type, food, category):
        super().__init__(type)
        self.food = food
        self.category = category

    def show(self):
        print("Pet Animal")
        print("Type:", self.type)
        print("Food:", self.food)
        print("Category:", self.category)

w1 = WildAnimal("Tiger", "Roar", "Orange")
p1 = PetAnimal("Dog", "Meat", "Domestic")

w1.show()

print()

p1.show()