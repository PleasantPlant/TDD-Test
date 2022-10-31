import unittest
from animal import Animal

class Test_animal(unittest.TestCase):

    def test_default_name_cat(self):
        cat = Animal("cat")

        self.assertEqual(cat, "Seymour")