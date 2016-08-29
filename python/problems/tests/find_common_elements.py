import unittest2

from problems.find_common_elements import get_common_elements
from utils.random_generators import array_of_random_integers


class ListTestCase(unittest2.TestCase):

    def _test_common(self, a1, a2):
        print ""
        print "First list:\t", a1
        print "Second list:\t", a2
        common_elements = get_common_elements(a1, a2)
        print "Common:\t\t", common_elements
        self.assertEqual(sorted(list(set(a1) & set(a2))), common_elements)
        return common_elements

    def test_basic(self):
        a1 = [1, 2, 3, 4, 5, 11]
        a2 = [1, 4, 8, 9, 10, 11, 11]
        self._test_common(a1, a2)

    def test_random_lists(self):
        a1 = array_of_random_integers(0, 20, 20)
        a1.sort()
        a2 = array_of_random_integers(3, 23, 25)
        a2.sort()
        self._test_common(a1, a2)

    def test_empty_lists(self):
        a1 = a2 = []
        self._test_common(a1, a2)

    def test_one_element_and_empty_list(self):
        a1 = [5]
        a2 = []
        self._test_common(a1, a2)

    def test_identical_lists(self):
        a1 = a2 = [1, 2, 3, 4, 5]
        self._test_common(a1, a2)

    def test_one_repeated_element(self):
        a1 = [1 for __ in range(10)]
        a2 = [0] + [1 for __ in range(9)]
        self._test_common(a1, a2)

if __name__ == '__main__':
    unittest2.main()
