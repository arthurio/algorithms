# Data Structure  | Time Complexity
# --------------------------------------------------------------------------------------------
#                 | Find Max | Extract Max | Increase Key | Insert    | Delete    | Merge
# Binary Heap     | O(1)     | O(log(n))   | O(log(n))    | O(log(n)) | O(log(n)) | O(m+n)
# Pairing Heap    | O(1)     | O(log(n))   | O(log(n))    | O(1)      | O(log(n)) | O(1)
# Binomial Heap   | O(1)     | O(log(n))   | O(log(n))    | O(1)      | O(log(n)) | O(log(n))
# Fibonacci Heap  | O(1)     | O(log(n))   | O(1)         | O(1)      | O(log(n)) | O(1)


import math


class HeapElement(object):
    """ Element of a Heap. It can be used in a array as is but needs to be decorated for a tree.

    Attributes:
        key: The value of held by the node.
    """
    def __init__(self, key=None):
        self.key = key

    def __repr__(self):
        return '%s(key=%r)' % (self.__class__.__name__, self.key)

    @property
    def left_child(self):
        raise NotImplementedError

    @property
    def right_child(self):
        raise NotImplementedError


class NodeHeapElement(HeapElement):
    """ Node used in our tree implementation of the Heap.

    Attributes:
        parent (NodeHeapElement: Parent node
        key: The value held by the node.
        left_child_node (NodeHeapElement):
        right_child_node (NodeHeapElement):
    """
    def __init__(self, key=None):
        super(NodeHeapElement, self).__init__(key)
        self._left_child = None
        self._right_child = None
        self._parent = None

    @property
    def left_child(self):
        return self._left_child

    @left_child.setter
    def left_child(self, node):
        '''
        Args:
            node (NodeHeapElement): new node
        '''
        self._left_child = node
        node.parent = self

    @property
    def right_child(self):
        return self._right_child

    @right_child.setter
    def right_child(self, node):
        '''
        Args:
            node (NodeHeapElement): new node
        '''
        self._right_child = node
        node.parent = self

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        '''
        Args:
            node (NodeHeapElement): new parent
        '''
        self._parent = node


class ArrayHeapElement(HeapElement):
    """ Node used in our tree implementation of the Heap.

    Attributes:
        key: The value of held by the node.
        index: Index in the array.
    """
    def __init__(self, key=None, index=0):
        super(ArrayHeapElement, self).__init__(key)
        self.index = index

    def __repr__(self):
        return '%s(key=%r, index=%r)' % (self.__class__.__name__, self.key, self.index)

    @property
    def left_child(self):
        return 2 * self.index + 1

    @property
    def right_child(self):
        return 2 * self.index + 2

    @property
    def parent(self):
        return int(math.floor((self.index - 1) / 2))


class HeapDataStructure(object):
    def __init__(self):
        self._size = 0

    def _is_empty(self):
        return self._size == 0

    def insert(self, key):
        raise NotImplementedError

    def to_array(self):
        raise NotImplementedError

    def swap(self, first_element, second_element):
        first_element.key, second_element.key = second_element.key, first_element.key

    def get_parent(self, element):
        raise NotImplementedError


class ArrayHeapDataStructure(HeapDataStructure):
    """ Simple array.

    The first (or last) element will contain the root. The next two elements of the array contain its children.
    The next four contain the four children of the two child nodes, etc.
    Thus the children of the node at position n would be at positions [...] 2n + 1 and 2n + 2 in a zero-based array.
    This allows moving up or down the tree by doing simple index computations.
    """
    def __init__(self):
        super(ArrayHeapDataStructure, self).__init__()
        self._array = []

    def __repr__(self):
        return '%s[%s]' % (self.__class__.__name__, ', '.join([repr(element) for element in self._array]))

    def to_array(self):
        return [element.key for element in self._array]

    def insert(self, key):
        """
        """
        new_element = ArrayHeapElement(key, self._size)
        self._array.append(
            new_element
        )
        self._size += 1
        return new_element

    def get_parent(self, element):
        if element.parent < 0:
            return None
        return self._array[element.parent]


class TreeHeapDataStructure(HeapDataStructure):
    def __init__(self):
        super(TreeHeapDataStructure, self).__init__()
        self._root = None

    def __repr__(self):
        return '[%s]' % ', '.join([repr(node) for node in self._get_all_nodes()])

    def to_array(self):
        return [node.key for node in self._get_all_nodes()]

    def _get_all_nodes(self):
        nodes = []
        queue = [self._root]
        while queue:
            node = queue.pop(0)
            nodes.append(node)
            for child in ['left_child', 'right_child']:
                child_node = getattr(node, child)
                if child_node:
                    queue.append(child_node)

        return nodes

    def insert(self, key):
        new_node = NodeHeapElement(key)
        if self._is_empty():
            self._root = new_node
        else:
            # We already have a root, find the first empty spot with a BFS iteration
            queue = [self._root]

            while queue:
                node = queue.pop(0)

                if not node.left_child:
                    node.left_child = new_node
                    break

                if not node.right_child:
                    node.right_child = new_node
                    break

                queue.append(node.left_child)
                queue.append(node.right_child)

        self._size += 1
        return new_node

    def get_parent(self, node):
        return node.parent


class HeapCondition(object):
    def compare(self, parent_key, child_key):
        raise NotImplementedError


class MinHeapCondition(HeapCondition):
    def compare(self, parent_key, child_key):
        return parent_key < child_key


class MaxHeapCondition(HeapCondition):
    def compare(self, parent_key, child_key):
        return parent_key > child_key


class Heap(object):
    """ Implementation of the Heap datastructure with an array.

    A heap is a specialized tree-based data structure that satisfies the heap property:
        If A is a parent node of B then the key (the value) of node A is ordered with respect to the key of node B
        with the same ordering applying across the heap.

    Source: https://en.wikipedia.org/wiki/Heap_(data_structure)

    Attributes:
        root (list)
    """
    def __init__(self, DataStructure, Condition):
        '''
        Args:
            DataStructure (Type): Must be subclass of HeapDataStructure
            Condition (Type): Must be subclass of HeapCondition
        '''
        assert issubclass(DataStructure, HeapDataStructure)
        assert issubclass(Condition, HeapCondition)
        self._data_structure = DataStructure()
        self._condition = Condition()
        self._size = 0

    def __repr__(self):
        return repr(self._data_structure)

    def to_array(self):
        return self._data_structure.to_array()

    # Creation (Class methods)
    @classmethod
    def create(cls, data_structure):
        """ Create an empty heap.

        Return:
            heap (Heap): Empty heap.
        """
        return cls(data_structure)

    @classmethod
    def heapify(cls, array):
        """ Create a heap out of given array of elements.

        Args:
            array (list): Array of elements.

        Return:
            heap (Heap): Heap containing all the elements of the array.
        """
        heap = cls()
        for key in array:
            heap.insert(key)
        return heap

    @classmethod
    def merge(cls, first_heap, second_heap):
        """ Joining two heaps to form a valid new heap containing all the elements of both,
            preserving the original heaps.

        Args:
            first_heap (Heap): first heap.
            second_heap (Heap): second heap.

        Return:
            heap (Heap): New heap containing of the elements of both heaps.
        """
        pass

    @classmethod
    def meld(cls, first_heap, second_heap):
        """ Joining two heaps to form a valid new heap containing all the elements of both,
            destroying the original heaps.

        Args:
            first_heap (Heap): first heap.
            second_heap (Heap): second heap.

        Return:
            heap (Heap): New heap containing of the elements of both heaps.
        """
        pass

    def _delete_key(self):
        """ Delete an arbitrary node (followed by moving last node and sifting to maintain heap)
        """
        pass

    def _shift_up(self, element):
        """ Move a node up in the tree, as long as needed.

        Used to restore heap condition after insertion.
        Called "sift" because node moves up the tree until it reaches the correct level, as in a sieve.
        """
        parent = self._data_structure.get_parent(element)
        while parent and not self._condition.compare(parent.key, element.key):
            self._data_structure.swap(parent, element)
            parent = self._data_structure.get_parent(parent)
            element = self._data_structure.get_parent(element)

    def _shift_down(self):
        """ Move a node down in the tree, similar to shift-up.

        Used to restore heap condition after deletion or replacement.
        """
        pass

    def _get_left_child(self, element):
        return self._data_structure.get_left_child(element)

    # Basic
    def insert(self, key):
        """ Add a key to the bottom level of the heap.

        1. Add the element to the bottom level of the heap.
        2. Compare the added element with its parent; if they are in the correct order, stop.
        3. If not, swap the element with its parent and return to the previous step.

        Args:
            key: Key to add in the heap.
        """
        element = self._data_structure.insert(key)
        self._shift_up(element)

    def extract(self):
        """ Extract the root element from the heap.

        Return:
            root (HeapElement): Remove the root from the heap and return it.
        """
        return self.data_structure.extract_root()

    def find(self):
        """ Return the value of the root.
        """
        return self.data_structure.get_root().key

    def delete(self):
        """ Remove the root element from the heap.
        """
        self.extract()

    def replace(self, key):
        """ Pop root and push a new key.

        More efficient than pop followed by push, since only need to balance once, not twice, and appropriate for
        fixed-size heaps.

        Args:
            key: Key to replace the root with.
        """
        root = self.extract()
        self.insert(root.key)

    # Inspection
    def size(self):
        """
        Return:
            size (int): Size of the heap.
        """
        return self._size

    def is_empty(self):
        """
        Return:
            is_empty (bool): return true if the heap is empty, false otherwise.
        """
        return self._size == 0


class BinaryHeap(object):
    """ A binary heap is defined as a binary tree with two additional constraints.

    Shape property: A binary heap is a complete binary tree; that is, all levels of the tree, except possibly the last
                    one (deepest) are fully filled, and, if the last level of the tree is not complete, the nodes of
                    that level are filled from left to right.
    Heap property: The key stored in each node is either greater than or equal to or less than or equal to the keys in
                   the node's children, according to some total order.

    https://en.wikipedia.org/wiki/Binary_heap

    Attribute:
        Heap
    """
    def __init__(self):
        self._heap = Heap()
