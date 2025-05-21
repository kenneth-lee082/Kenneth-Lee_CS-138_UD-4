# documentary.py
# Author: Kenneth Lee
# Date: 2025-05-19
# Description: This file defines the Documentary subclass of Movie. It stores
# whether the film is based on real events and includes methods to express this
# in its string representation.

from movie import Movie

class Documentary(Movie):
    """
    Represents a documentary film. Tracks whether the content is
    based on true events and reflects that in string output.
    """
    def __init__(self, title, director, year, is_real):
        super().__init__(title, director, "Documentary", year)
        self._is_real = is_real

    def is_based_on_true_story(self):
        """Returns True if the documentary is based on real events."""
        return self._is_real

    def get_is_real(self): return self._is_real
    def set_is_real(self, value): self._is_real = value

    def __str__(self):
        truth_str = "True Story" if self.is_based_on_true_story() else "Fictional Documentary"
        return f"{super().__str__()} | {truth_str}"
