class Animal():

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_name(self):
        print(f"My name is {self.name}, I am a {type(self).__name__}")

    def eat(self):
        print('I am eating')

    def make_sound(self):
        print('Some voice')

    def get_benefits(self):
        print('Take something')


class Cow(Animal):

    def get_benefits(self):
        print('Take the milk')

    def make_sound(self):
        print('Mu-mu')


class Goose(Animal):

    def get_benefits(self):
        print('Take the egg')

    def make_sound(self):
        print('Honk-honk')


class Sheep(Animal):

    def get_benefits(self):
        print('Take the wool')

    def make_sound(self):
        print('Baa-baa')


class Chicken(Animal):

    def get_benefits(self):
        print('Take the egg')

    def make_sound(self):
        print('Cluck-cluck')


class Goat(Animal):

    def get_benefits(self):
        print('Take the milk')

    def make_sound(self):
        print('Baa-baa')


class Duck(Animal):

    def get_benefits(self):
        print('Take the egg')

    def make_sound(self):
        print('Quack-quack')


animals = [
    Goose('Белый', 5),
    Goose('Серый', 7),
    Cow('Манька', 120),
    Sheep('Барашек', 40),
    Sheep('Кудрявый', 55),
    Chicken('Ко-Ко', 3),
    Chicken('Кукареку', 4),
    Goat('Рога', 25),
    Goat('Копыта', 30),
    Duck('Кряква', 4)
]

if __name__ == '__main__':
    heaviest_animal = {'name': '', 'weight': 0}
    common_weight = 0
    for animal in animals:
        animal.get_name()
        animal.make_sound()
        animal.eat()
        animal.get_benefits()

        common_weight += animal.weight
        if animal.weight > heaviest_animal['weight']:
            heaviest_animal['weight'] = animal.weight
            heaviest_animal['name'] = animal.name
        print()
    print(f"Общий вес животных: {common_weight}")
    print(f"Самое тяжелое животное: {heaviest_animal['name']}. Вес: {heaviest_animal['weight']}")
