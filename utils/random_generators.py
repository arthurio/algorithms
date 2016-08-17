import random


def array_of_random_integers(start, finish, size):
    return [random.randrange(start, finish) for __ in range(size)]
