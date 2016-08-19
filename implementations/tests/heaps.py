import unittest2

import heapq
import heapq_max

from implementations.heaps import Heap
from implementations.heaps import ArrayHeapDataStructure
from implementations.heaps import MinHeapCondition
from implementations.heaps import MaxHeapCondition
from implementations.heaps import TreeHeapDataStructure
from utils.random_generators import array_of_random_integers


KEYS = array_of_random_integers(0, 10, 15)


class MinHeapTestCase(unittest2.TestCase):

    def setUp(self):
        self.python_heap = []

    def _insert(self, heap, key):
        heapq.heappush(self.python_heap, key)
        heap.insert(key)

    def _test_insert(self, heap):
        for key in KEYS:
            self._insert(heap, key)

        self.assertEqual(
            self.python_heap,
            heap.to_array()
        )


class MinArrayHeapTestCase(MinHeapTestCase):

    def setUp(self):
        super(MinArrayHeapTestCase, self).setUp()
        self.heap = Heap(ArrayHeapDataStructure, MinHeapCondition)

    def test_insert(self):
        self._test_insert(self.heap)


class MinTreeHeapTestCase(MinHeapTestCase):

    def setUp(self):
        super(MinTreeHeapTestCase, self).setUp()
        self.heap = Heap(TreeHeapDataStructure, MinHeapCondition)

    def test_insert(self):
        self._test_insert(self.heap)


class MaxHeapTestCase(unittest2.TestCase):

    def setUp(self):
        self.python_heap = []

    def _insert(self, heap, key):
        heapq_max.heappush_max(self.python_heap, key)
        heap.insert(key)

    def _test_insert(self, heap):
        for key in KEYS:
            self._insert(heap, key)

        self.assertEqual(
            self.python_heap,
            heap.to_array()
        )


class MaxArrayHeapTestCase(MaxHeapTestCase):

    def setUp(self):
        super(MaxArrayHeapTestCase, self).setUp()
        self.heap = Heap(ArrayHeapDataStructure, MaxHeapCondition)

    def test_insert(self):
        self._test_insert(self.heap)


class MaxTreeHeapTestCase(MaxHeapTestCase):

    def setUp(self):
        super(MaxTreeHeapTestCase, self).setUp()
        self.heap = Heap(TreeHeapDataStructure, MaxHeapCondition)

    def test_insert(self):
        self._test_insert(self.heap)


if __name__ == '__main__':
    unittest2.main()
