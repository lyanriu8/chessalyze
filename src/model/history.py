"""History"""

from reader import Reader
from game import Game


class History:
    """History of given player
    """

    def __init__(self, username):
        """Constructor for sinlge history object

        Args:
            username (string): Username inputed
        """
        self.reader = Reader(username)
        self.history = []
        self.set_history()

    def set_history(self):
        """Given
        """

        for key, value in self.reader.sorted_archive.items():
            game = Game(key, value)
            self.history.append(game)


# ryan = History("lyanriu8")
# print(ryan.history)
