"""Represents a game replay system"""


class Game:
    """Represents a single game object"""

    def __init__(self, key, value):
        """Constructor

        Args:
            key (string): represents key of key-value pair
            value (string): represents value of key-value pair
        """

        (self.event, self.site, self.date, self.round_num, self.white, self.black, self.result,
         self.current_pos, self.timezone, self.eco, self.eco_url, self.utc_date, self.utc_time,
         self.white_elo, self.black_elo, self.time_control, self.termination, self.start_time,
         self.end_date, self.end_time, self.link) = key.split("\n")

        self.game_replay = GameReplay(value)


class GameReplay:
    """Represents a single game replay object"""

    def __init__(self, value):
        """Constructor

        Args:
            value (string): History of game in pgn
        """

        self.game_replay = value
