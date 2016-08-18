import unittest2

from implementations.heaps import Heap
from implementations.heaps import HeapTreeDataStructure


class HeapArrayTestCase(unittest2.TestCase):

    def setUp(self):
        self.heap = Heap.create()

    def test_insert(self):
        self.heap.insert(1)
        self.heap.insert(2)
        self.heap.insert(4)

        print self.heap


class HeapTreeTestCase(unittest2.TestCase):

    def setUp(self):
        self.heap = Heap.create(HeapTreeDataStructure())

    def test_insert(self):
        self.heap.insert(1)
        self.heap.insert(2)
        self.heap.insert(4)

        print self.heap

if __name__ == '__main__':
    unittest2.main()
