class Cell(object):
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value) if self.value is not None else ' '


def _check_is_within_bounds(f):
    def wrapper(self, x, y, *args):
        if not(0 <= x < self.rows) or not(0 <= y < self.cols):
            raise self.OutOfBoundError

        return f(self, x, y, *args)
    return wrapper


class Board(object):

    class OutOfBoundError(Exception):
        pass

    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._grid = [[Cell() for __ in range(cols)] for __ in range(rows)]

    def __str__(self):
        board = ''
        for row, cols in enumerate(self._grid):
            col_str = ' '
            for col, cell in enumerate(cols):
                col_str = '%s%s%s' % (col_str, str(cell), ' | ' if col < self.cols - 1 else '')

            print col_str
            if row < self.rows - 1:
                print ' '.join(['___' for __ in range(self._cols)])
        return board

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    @_check_is_within_bounds
    def get_cell(self, x, y):
        return self._grid[x][y]

    def get_cell_value(self, x, y):
        try:
            return self.get_cell(x, y).value
        except self.OutOfBoundError:
            return None

    @_check_is_within_bounds
    def set_cell_value(self, x, y, value):
        self.get_cell(x, y).value = value


class Game(object):
    def add_player(self, player):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    def play(self, x, y):
        raise NotImplementedError


class TicTacToe(Game):
    ROWS = 3
    COLS = 3
    ALIGNED_TOKENS_TO_WIN = 3
    PLAYER_LIMIT = 2
    TOKENS = [
        'X',
        'O',
    ]

    NORTH = 'n'
    WEST = 'w'
    SOUTH = 's'
    EAST = 'e'
    NORTH_EAST = NORTH + EAST
    NORTH_WEST = NORTH + WEST
    SOUTH_EAST = SOUTH + EAST
    SOUTH_WEST = SOUTH + WEST

    DIRECTIONS = {
        NORTH: (0, 1),
        WEST: (-1, 0),
        SOUTH: (0, -1),
        EAST: (1, 0),
        NORTH_EAST: (1, 1),
        NORTH_WEST: (-1, 1),
        SOUTH_EAST: (1, -1),
        SOUTH_WEST: (-1, -1),
    }

    HORIZONTAL = 'h'
    VERTICAL = 'v'
    DIAGONAL_1 = 'd1'
    DIAGONAL_2 = 'd2'

    ALIGNMENTS = {
        DIAGONAL_1: (DIRECTIONS[SOUTH_WEST], DIRECTIONS[NORTH_EAST]),
        DIAGONAL_2: (DIRECTIONS[NORTH_WEST], DIRECTIONS[SOUTH_EAST]),
        HORIZONTAL: (DIRECTIONS[WEST], DIRECTIONS[EAST]),
        VERTICAL: (DIRECTIONS[NORTH], DIRECTIONS[SOUTH]),
    }

    class TooManyPlayersError(Exception):
        pass

    class GameHasAlreadyStartedError(Exception):
        pass

    class MissingPlayersError(Exception):
        pass

    class NotPlayerTurnError(Exception):
        pass

    class CellNotEmptyError(Exception):
        pass

    class GameOverError(Exception):
        pass

    class GameNotStartedError(Exception):
        pass

    def __init__(self):
        self._board = Board(self.ROWS, self.COLS)
        self._players = [None for __ in range(self.PLAYER_LIMIT)]
        self._started = False
        self._current_player = None
        self._winner = None

    def __str__(self):
        return str(self._board)

    @property
    def players(self):
        return self._players

    @property
    def board(self):
        return self._board

    @property
    def player_limit(self):
        return len(self.players)

    @property
    def is_started(self):
        return self._started

    @property
    def winner(self):
        return self._winner

    def get_token(self, player):
        return self.TOKENS[self.players.index(player)]

    def can_start(self):
        return None not in self.players

    def add_player(self, player):
        if self.is_started:
            raise self.GameHasAlreadyStartedError

        if self.can_start():
            raise self.TooManyPlayersError

        self.players.index(None)
        self._players[self.players.index(None)] = player

    def start(self):
        if not self.can_start():
            raise self.MissingPlayersError

        if self.is_started:
            raise self.GameHasAlreadyStartedError

        self._current_player = self.players[0]
        self._started = True

    def play(self, x, y, token):
        '''
        Returns:
            is_winner (boolean): True if the play made the player win, False otherwise
        '''
        if self._winner is not None:
            raise self.GameOverError

        if not self._started:
            raise self.GameNotStartedError

        if token not in self.TOKENS:
            raise self.InvalidTokenError

        current_player_index = self.TOKENS.index(token)
        player = self.players[current_player_index]
        if player != self._current_player:
            raise self.NotPlayerTurnError

        if self._board.get_cell_value(x, y) is not None:
            raise self.CellNotEmptyError

        self._board.set_cell_value(x, y, token)

        # +1 to take current token into account
        if self._won_the_game(x, y, token):
            self._winner = player
            return True

        self._current_player = self.players[(current_player_index + 1) % self.player_limit]
        return False

    def _won_the_game(self, x, y, token):
        count_by_alignment = {
            self.HORIZONTAL: 0,
            self.VERTICAL: 0,
            self.DIAGONAL_1: 0,
            self.DIAGONAL_2: 0,
        }

        queue = [(1, self.ALIGNMENTS)]  # look in all directions on the first pass

        while queue:
            distance, alignments = queue.pop(0)
            for alignment, directions in alignments.items():

                new_directions = []

                for direction in directions:
                    neighbor_x, neighbor_y = direction

                    if self._board.get_cell_value(x + distance * neighbor_x, y + distance * neighbor_y) == token:
                        number_of_neighbors = count_by_alignment[alignment] + 1

                        # If me + my neighbors == number of aligned cells to win
                        if number_of_neighbors + 1 == self.ALIGNED_TOKENS_TO_WIN:
                            return True

                        count_by_alignment[alignment] = number_of_neighbors
                        new_directions.append(direction)

                if new_directions:
                    queue.append((distance + 1, {alignment: new_directions}))

        return False


class Player(object):
    class GameIsFullError(Exception):
        pass

    class NoGameJoinedError(Exception):
        pass

    def __init__(self, name):
        self.name = name
        self.game = None

    def __str__(self):
        return str(self.name)

    def join(self, game):
        try:
            game.add_player(self)
            self.game = game
        except (game.GameHasAlreadyStartedError, game.TooManyPlayersError):
            raise self.GameIsFullError

    def play(self, x, y):
        if self.game is None:
            raise self.NoGameJoinedError

        value = self.game.get_token(self)
        self.game.play(x, y, value)
