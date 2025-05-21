# feature_film.py
# Author: Kenneth Lee
# Date: 2025-05-19
# Description: This file defines the FeatureFilm subclass of Movie, adding
# attributes such as duration and rating, along with methods for evaluating
# length and family-friendliness.

from movie import Movie

class FeatureFilm(Movie):
    """
    A subclass of Movie that represents a full-length feature film.
    Adds attributes like duration and rating and provides methods to
    evaluate length and family accessibility.
    """
    def __init__(self, title, director, year, duration, rating):
        super().__init__(title, director, "Feature Film", year)
        self._duration = duration
        self._rating = rating

    def is_long_film(self):
        """Returns True if the movie is at least 120 minutes long."""
        return self._duration >= 120

    def is_family_friendly(self):
        """Returns True if the rating is G or PG."""
        return self._rating in ['G', 'PG']

    def get_duration(self): return self._duration
    def set_duration(self, value): self._duration = value

    def get_rating(self): return self._rating
    def set_rating(self, value): self._rating = value

    def __str__(self):
        long_str = "Long Film" if self.is_long_film() else "Short Film"
        family_str = "Family Friendly" if self.is_family_friendly() else "Not for Kids"
        return f"{super().__str__()} | {long_str}, {family_str} | Duration: {self._duration} min | Rating: {self._rating}"
