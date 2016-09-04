import unittest2

from problems.spiral import position_of_n
from problems.spiral import spiral_formula


class SpiralTestCase(unittest2.TestCase):

    def test_n_6(self):
        starting_point = (0, 0)
        n = 6

        position = position_of_n(starting_point, spiral_formula, n)
        self.assertEqual((2, 2), position)
