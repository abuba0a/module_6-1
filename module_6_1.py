class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    edible = False
    pass


class Fruit(Plant):
    edible = True
    pass


class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.food = Plant
        self.name = name


class Mammal(Animal):
    alive = True

    def eat(self, food):
        self.food = Plant
        if food is Fruit(Plant):
            print(self.name, 'съел', food.name)
            fed = True
        else:
            print(self.name, 'не стал есть', food.name)
            alive = False


class Predator(Animal):
    alive = True

    def eat(self, food):
        self.food = Plant
        if food is Plant:
            print(self.name, 'не стал есть', food.name)
            alive = False


a1 = Predator('Волк')
a2 = Mammal('Бык')
p1 = Flower('Цветок')
p2 = Fruit('Апельсин')

print(a1.name)
print(a2.name)
print(p1.name)
print(p2.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
