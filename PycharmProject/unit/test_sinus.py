import math
import unittest

from sinus import sinus


class SinusTestCase(unittest.TestCase):
    def test_poprawny_wynik(self):
        wynik = sinus(0)
        self.assertAlmostEqual(sinus(0.), 0.)
        self.assertAlmostEqual(sinus(math.pi/4), math.sqrt(2.)/2)
        self.assertAlmostEqual(sinus(math.pi/2), 1.0)


if __name__ == '__main__':
    unittest.main()
