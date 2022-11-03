import unittest
from animal import Animal


class Test_animal(unittest.TestCase):
    def test_default_name_cat(self):
        cat = Animal("cat")

        self.assertEqual(cat.name, "Seymour")

    def test_default_name_dog(self):
        dog = Animal("dog")

        self.assertEqual(dog.name, "Spot")

    def test_animal_custom_name(self):
        dog = Animal("dog")
        cat = Animal("cat")
        dog.name = "NotSpot"
        cat.name = "Garfield"
        self.assertEqual(dog.name, "NotSpot")
        self.assertEqual(cat.name, "Garfield")

    def test_smallCat(self):
        cat = Animal("cat")
        cat.size = "small"
        self.assertEqual(cat.speak(), "meow")

    def test_notSmallCat(self):
        cat = Animal("cat")
        cat2 = Animal("cat")
        cat.size = "medium"
        cat2.size = "Large"
        self.assertEqual(cat.speak(), "Meow!")
        self.assertEqual(cat2.speak(), "Meow!")

    ##It seems to me that the dog sizes and noises are mismatched...
    def test_smallDog(self):
        dog = Animal("dog")
        dog.size = "small"
        self.assertEqual(dog.speak(), "bow wow")

    def test_mediumDog(self):
        dog = Animal("dog")
        dog.size = "medium"
        self.assertEqual(dog.speak(), "Ruff ruff")

    def test_largeDog(self):
        dog = Animal("dog")
        dog.size = "large"
        self.assertEqual(dog.speak(), "arf arf")

    def test_youngAnimal(self):
        animal = Animal("cat")
        animal.name = "x"
        animal.age = 10
        self.assertEqual(animal.describe(), "x is young")

    def test_oldAnimal(self):
        animal = Animal("cat")
        animal.name = "x"
        animal.age = 11
        self.assertEqual(animal.describe(), "x is old")
