import math
import unittest

from sinus import sinus


class SinusTestCase(unittest.TestCase):
    def test_poprawny_wynik(self):
        wynik = sinus(0)
        self.assertEqual(wynik, 0.)
        self.assertEqual(sinus(math.pi / 2), 1.0)


if __name__ == '__main__':
    unittest.main()
