import unittest

from animal import Animal


class Test_animal(unittest.TestCase):
    def test_default_name_cat(self):

        # GIVEN - a new instance of Animal whose type is "cat"

        cat = Animal("cat")

        # WHEN - no action

        pass

        # THEN - the name property of cat is "Seymour"

        self.assertEqual(cat.name, "Seymour")

    def test_default_name_dog(self):

        # GIVEN - a new instance of Animal whose type is "dog"

        dog = Animal("dog")

        # WHEN - no action

        pass

        # THEN - the name property of cat is "Seymour"

        self.assertEqual(dog.name, "Spot")

    def test_provided_name(self):

        # GIVEN - a new instance of Animal whose type is anything, in this case "dog". And whose name is assigned explicitly.

        assigned_name = "Killer"

        dog = Animal("dog")

        dog.name = assigned_name

        # WHEN - no action

        pass

        # THEN - the name property is the assigned name

        self.assertEqual(dog.name, assigned_name)

    def test_cat_speak(self):

        # GIVEN - a new instance of Animal whose type is "cat" and size is 'small'

        cat1 = Animal("cat")

        cat1.size = "small"

        # WHEN - we call speak()

        words1 = cat1.speak()

        # THEN - return value = "meow"

        self.assertEqual(words1, "meow")

        # GIVEN - a new instance of Animal whose type is "cat" and size is NOT 'small'

        cat2 = Animal("cat")

        cat2.size = "medium"

        # WHEN - we call speak()

        words2 = cat2.speak()

        # THEN - return value = "MEOW!"

        self.assertEqual(words2, "MEOW!")

    def test_dog_speak(self):

        # GIVEN - a new instance of Animal whose type is "dog" and size is 'small'

        dog1 = Animal("dog")

        dog1.size = "small"

        # WHEN - we call speak()

        words1 = dog1.speak()

        # THEN - return value = "bow wow"

        self.assertEqual(words1, "bow wow")

        # GIVEN - a new instance of Animal whose type is "dog" and size is 'medium'

        dog2 = Animal("dog")

        dog2.size = "medium"

        # WHEN - we call speak()

        words2 = dog2.speak()

        # THEN - return value = "Ruff ruff"

        self.assertEqual(words2, "Ruff ruff")

        # GIVEN - a new instance of Animal whose type is "dog" and size is not 'small' or 'medium'

        dog3 = Animal("dog")

        dog3.size = "notsmallormedium"

        # WHEN - we call speak()

        words3 = dog3.speak()

        # THEN - return value = "arf arf"

        self.assertEqual(words3, "arf arf")

    def test_age(self):

        # GIVEN - a new instance of Animal whose type is anything, in this case "dog" and whose age is less than 10 (test with '9')

        dog1 = Animal("dog")

        dog1.age = 9

        # WHEN - we call describe()

        desc1 = dog1.describe()

        # THEN - return "[name] is young"

        self.assertEqual(desc1, f"{dog1.name} is young")

        # GIVEN - a new instance of Animal whose type is anything, in this case "dog" and whose age is NOT less than 10 (test with '10')

        dog2 = Animal("dog")

        dog2.age = 10

        # WHEN - we call describe()

        desc2 = dog2.describe()

        # THEN - return "[name] is young"

        self.assertEqual(desc2, f"{dog2.name} is old")
