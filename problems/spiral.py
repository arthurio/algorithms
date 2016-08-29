import math


def position_of_n(starting_point, formula, n):
    position = starting_point
    for i in range(n + 1):
        position = formula(position, i)

    return position


def spiral_formula(start, n):
    translation = int(math.ceil(n / float(2)))
    direction = (2 * (translation % 2) - 1)
    axis = 1 - (n % 2)

    new_position = [None, None]
    new_position[axis] = start[axis]
    new_position[1 - axis] = start[1 - axis] + (direction * translation)
    return new_position


if __name__ == '__main__':
    ''' Spiral looks as follow:


                        |
                        |
                     ___|________
                    |   |        |
                    |   |___     |
                    |   |   |    |
     _______________|___|___|____|___________
                    |   |   |    .
                    |___|___|    .
                        |        .

    Given n, the nth edge, write a function that returns it's position.
         position  translation  translation from root
    n0 = (0, 0)    (0, 0)
    n1 = (0, 1)    (0, 1)
    n2 = (1, 1)    (1, 0)
    n3 = (1, -1)   (0, -2)
    n4 = (-1, -1)  (-2, 0)
    n5 = (-1, 2)   (0, 3)
    n6 = (2, 2)    (3, 0)
    '''

    starting_point = (0, 0)
    n = 6

    position = position_of_n(starting_point, spiral_formula, n)
    print 'n%s = %s' % (n, position)
