import unittest2

from problems.shortest_path_in_matrix import find_shortest_path
from problems.shortest_path_in_matrix import START as S
from problems.shortest_path_in_matrix import END as E


class MatrixTestCase(unittest2.TestCase):
    def _print_matrix(self, matrix):
        print ""
        for row in matrix:
            print '|'.join([' %s ' % value for value in row])

    def _test_matrix(self, matrix):
        self._print_matrix(matrix)
        path = find_shortest_path(matrix)

        print "path:", path
        print "length:", len(path)

        return path


class UnvalidMatrixTestCase(MatrixTestCase):

    def test_empty(self):
        matrix = [[]]
        with self.assertRaises(AssertionError) as error:
            self._test_matrix(matrix)
        print error.exception

    def test_unvalid_path(self):
        matrix = [
            [1, 1, 1, 1, 1, 1, 1, S],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 1],
            [0, 1, 1, 1, 0, 0, 0, 0],  # There is a hole
            [0, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [E, 1, 1, 1, 1, 1, 1, 1],
        ]
        with self.assertRaises(AssertionError) as error:
            self._test_matrix(matrix)
        print error.exception

    def test_no_path(self):
        matrix = [
            [S, 0, 0],
            [0, 0, 0],
            [0, 0, E],
        ]
        with self.assertRaises(AssertionError) as error:
            self._test_matrix(matrix)
        print error.exception


class ValidMatrixTestCase(MatrixTestCase):

    def test_start_and_end_only(self):
        matrix = [
            [S, E],
        ]
        path = self._test_matrix(matrix)
        self.assertEqual([(0, 0), (0, 1)], path)
        self.assertEqual(2, len(path))

    def test_simple(self):
        matrix = [
            [1, 1, 1, 1, 1, 1, 1, S],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 1],
            [0, 1, 1, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [E, 1, 1, 1, 1, 1, 1, 1],
        ]
        path = self._test_matrix(matrix)
        self.assertEqual([
            (0, 7),
            (1, 7),
            (2, 7),
            (3, 7),
            (4, 7),
            (5, 7),
            (6, 7),
            (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (7, 0),
        ], path)
        self.assertEqual(15, len(path))

    def test_unequal_width_of_rows(self):
        matrix = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, S],
            [1, 1, 0, 0, 0, 0, 1, 1],
            [0, 1, 1, 1, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [E, 1, 1, 1, 1, 1, 1, 1],
        ]
        path = self._test_matrix(matrix)
        self.assertEqual([
            (1, 7),
            (2, 7), (2, 6),
            (3, 6),
            (4, 6), (4, 7),
            (5, 7),
            (6, 7),
            (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (7, 0)
        ], path)
        self.assertEqual(16, len(path))

    def test_starting_point_not_0_0(self):
        matrix = [
            [1, 1, 1, 1, 1, 1, 1, S],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 1],
            [0, 1, 1, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [E, 1, 1, 1, 1, 1, 1, 1],
        ]
        path = self._test_matrix(matrix)
        self.assertEqual([
            (0, 7),
            (1, 7),
            (2, 7),
            (3, 7),
            (4, 7),
            (5, 7),
            (6, 7),
            (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (7, 0)
        ], path)
        self.assertEqual(15, len(path))

    def test_multiple_starts(self):
        matrix = [
            [1, 1, 1, 1, 1, 1, 1, S],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 1],
            [0, 1, S, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [E, 1, 1, 1, 1, 1, 1, 1],
        ]
        path = self._test_matrix(matrix)
        self.assertEqual([
            (3, 2), (3, 3),
            (4, 3),
            (5, 3), (5, 2), (5, 1), (5, 0),
            (6, 0), (7, 0)
        ], path)
        self.assertEqual(9, len(path))

    def test_multiple_ends(self):
        matrix = [
            [1, 1, 1, 1, 1, 1, 1, S],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 1],
            [0, 1, E, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [E, 1, 1, 1, 1, 1, 1, 1],
        ]
        path = self._test_matrix(matrix)
        self.assertEqual([
            (0, 7), (0, 6), (0, 5), (0, 4), (0, 3), (0, 2), (0, 1), (0, 0),
            (1, 0),
            (2, 0), (2, 1),
            (3, 1), (3, 2)
        ], path)
        self.assertEqual(13, len(path))

    def test_multiple_start_and_ends(self):
        matrix = [
            [1, 1, 1, 1, 1, 1, 1, S],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 1],
            [0, 1, E, 1, 0, 0, 0, S],
            [0, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [E, 1, 1, 1, 1, 1, 1, 1],
        ]
        path = self._test_matrix(matrix)
        self.assertEqual([
            (3, 7),
            (4, 7),
            (5, 7),
            (6, 7),
            (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (7, 0)
        ], path)
        self.assertEqual(12, len(path))

    def test_similar_shortest_paths(self):
        # Matrix with similar shortest path
        matrix = [
            [1, 1, 1, 1, 1, 1, 1, S],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [E, 1, 1, 1, 1, 1, 1, 1],
        ]
        path = self._test_matrix(matrix)
        self.assertEqual([
            (0, 7),
            (1, 7),
            (2, 7),
            (3, 7),
            (4, 7),
            (5, 7),
            (6, 7),
            (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (7, 0)
        ], path)
        self.assertEqual(15, len(path))

if __name__ == '__main__':
    unittest2.main()
