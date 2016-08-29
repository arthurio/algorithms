import unittest2


from problems.tictactoe import Player
from problems.tictactoe import TicTacToe


class TicTacToeTestCase(unittest2.TestCase):

    def setUp(self):
        self.game = TicTacToe()
        self.player1 = Player("Player1")
        self.player2 = Player("Player2")

    def test_simple_play(self):
        self.player1.join(self.game)
        self.player2.join(self.game)

        self.game.start()

        self.player1.play(0, 1)
        self.player2.play(1, 1)

        self.player1.play(2, 1)
        self.player2.play(1, 0)

        self.player1.play(2, 2)
        self.player2.play(1, 2)

        self.assertEqual(self.player2, self.game.winner)


# TODO assert all the exceptions about invalid plays
