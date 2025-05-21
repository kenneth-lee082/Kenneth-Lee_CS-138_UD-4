# drama_series.py
# Author: Kenneth Lee
# Date: 2025-05-19
# Description: This file defines the DramaSeries subclass of Movie. It includes
# attributes for season and episodes, and provides methods to determine if the
# series is a miniseries and estimate its total runtime.

from movie import Movie

class DramaSeries(Movie):
    """
    Represents a drama series with seasons and episode count.
    Includes logic to determine miniseries status and estimate runtime.
    """
    def __init__(self, title, director, year, season, episodes):
        super().__init__(title, director, "Drama Series", year)
        self._season = season
        self._episodes = episodes

    def is_miniseries(self):
        """Returns True if the series has 8 or fewer episodes."""
        return self._episodes <= 8

    def total_runtime(self, avg_minutes=45):
        """Estimates the total runtime based on average episode length."""
        return self._episodes * avg_minutes

    def get_season(self): return self._season
    def set_season(self, value): self._season = value

    def get_episodes(self): return self._episodes
    def set_episodes(self, value): self._episodes = value

    def __str__(self):
        mini_str = "Miniseries" if self.is_miniseries() else "Full Series"
        return f"{super().__str__()} | {mini_str} | Season: {self._season} | Episodes: {self._episodes} | Est. Runtime: {self.total_runtime()} min"

