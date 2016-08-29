import unittest2

from copy import copy
from implementations.sorts import bubble_sort
from implementations.sorts import insertion_sort
from implementations.sorts import merge_sort_in_place
from implementations.sorts import quicksort
from utils.random_generators import array_of_random_integers


class SortTestCase(unittest2.TestCase):

    def setUp(self):
        self.unsorted = array_of_random_integers(0, 10, 15)

    def _test_sort(self, algorithm):
        print algorithm.__name__
        sorted_array = copy(self.unsorted)
        algorithm(sorted_array)
        print self.unsorted, "-->", sorted_array
        self.assertEqual(sorted(self.unsorted), sorted_array)


class InsertionSortTestCase(SortTestCase):
    def test_sorting(self):
        self._test_sort(insertion_sort)


class QuickSortTestCase(SortTestCase):
    def test_sorting(self):
        self._test_sort(quicksort)


class MergeSortInPlaceTestCase(SortTestCase):
    def test_sorting(self):
        self._test_sort(merge_sort_in_place)


class BubbleSortTestCase(SortTestCase):
    def test_sorting(self):
        self._test_sort(bubble_sort)

if __name__ == '__main__':
    unittest2.main()
