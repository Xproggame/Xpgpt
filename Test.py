import unittest
from Enregistrement import assemblement, separation


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertListEqual(separation("salut au revoir bonne nuit"), [["au", "salut"], ["revoir", "au"], ["bonne", "revoir"], ["nuit", "bonne"]])


if __name__ == '__main__':
    unittest.main()
