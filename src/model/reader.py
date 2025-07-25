"""json reader of chess.com api"""

# pylint: disable=line-too-long

import requests


class Reader:
    """Reader reads api data and transforms it into useable information"""

    BASE_URL = "https://api.chess.com/pub/player/"

    HEADERS = {
        "User-Agent": "tool/1.2 (username: lyanriu8; contact: Ryanliu103@gmail.com)"}

    def __init__(self, username):
        self.username = username
        self.sorted_archive = {}
        self.sort_archive()

    def get_base_archive(self):
        """EFFECTS: retrieves archives for given player username"""

        url = f"{self.BASE_URL}{self.username}/games/archives"

        response = requests.get(url, headers=self.HEADERS, timeout=10)

        archive = response.json()
        return archive

    def sort_archive(self):
        """EFFECTS: creates sorted player archive"""

        base_archive = self.get_base_archive()["archives"]

        for month_archive_url in base_archive:
            response = requests.get(
                month_archive_url, headers=self.HEADERS, timeout=10)

            month_games = response.json()

            for g in month_games["games"]:
                pgn = g["pgn"]

                info, history = pgn.split("\n\n")

                self.sorted_archive[info] = history


reader = Reader("lyanriu8")
print(type(reader.sorted_archive))

for key, value in reader.sorted_archive.items():
    print(key)
    print(value)
    print("\n")
