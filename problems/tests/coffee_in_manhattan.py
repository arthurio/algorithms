import unittest2


from copy import deepcopy
from problems.coffee_in_manhattan import o_n_2
from problems.coffee_in_manhattan import o_n_log_n
# from utils.matrix import print_matrix


class CoffeeShopTestCase(unittest2.TestCase):

    def _test_algo(self, matrix, people, algo, solution):
        m = deepcopy(matrix)
        # print_matrix(m)
        best_intersection = algo(m, people)

        # print 'best intersection: %s' % str(best_intersection)
        # x, y = best_intersection
        # m[x][y] = 'o'
        # print_matrix(m)
        self.assertEqual(solution, best_intersection)

    def test_simple_matrix(self):
        people = [
            (0, 0), (0, 2),
            (2, 0), (2, 2),
        ]
        matrix = []
        matrix_length = 3
        for row in range(matrix_length):
            matrix.append([])
            for col in range(matrix_length):
                matrix[row].append('x' if (row, col) in people else ' ')
        '''
              0   1   2
          0 | x | - | x |
          1 | - | - | - |
          2 | x | - | x |

        people = (0, 0) (0, 2) (2, 0) (2, 2)
        xs = 0 0 2 2
                ^
        ys = 0 0 2 2
                ^
        best_intersection = (1, 1)
        '''
        solution = (1, 1)
        self.test_algo(matrix, people, o_n_2, solution)
        self.test_algo(matrix, people, o_n_log_n, solution)

    def test_large_matrix(self):
        people = [
            (0, 0), (0, 2), (0, 7),
            (1, 3), (1, 6),
            (2, 1), (2, 2),
            (3, 0), (3, 2), (3, 7),
            (4, 3), (4, 6),
            (5, 1), (5, 2),
            (6, 0), (6, 2), (6, 7),
            (7, 3), (7, 6),
            (8, 1), (8, 2),
            (9, 0), (9, 2), (9, 7),
        ]
        matrix = []
        matrix_length = 10
        for row in range(matrix_length):
            matrix.append([])
            for col in range(matrix_length):
                matrix[row].append('x' if (row, col) in people else ' ')
        '''
              0   1   2   3   4   5   6   7   8   9
          0 | x | - | x | - | - | - | - | x | - | - |
          1 | - | - | - | x | - | - | x | - | - | - |
          2 | - | x | x | - | - | - | - | - | - | - |
          3 | x | - | x | - | - | - | - | x | - | - |
          4 | - | - | - | x | - | - | x | - | - | - |
          5 | - | x | x | - | - | - | - | - | - | - |
          6 | x | - | x | - | - | - | - | x | - | - |
          7 | - | - | - | x | - | - | x | - | - | - |
          8 | - | x | x | - | - | - | - | - | - | - |
          9 | x | - | x | - | - | - | - | x | - | - |
        '''
        solution = (4, 2)
        self.test_algo(matrix, people, o_n_2, solution)
        self.test_algo(matrix, people, o_n_log_n, solution)
