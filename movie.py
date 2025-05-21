# movie.py
# Author: Kenneth Lee
# Date: 2025-05-19
# Description: This file defines the base Movie class, which holds shared attributes
# and methods for all movie-related media. All genre-specific subclasses inherit from this.

class Movie:
    """
    Base class for all types of movies. Contains general information
    such as title, director, genre, and release year.
    """
    def __init__(self, title, director, genre, year):
        self._title = title
        self._director = director
        self._genre = genre
        self._year = year

    def __str__(self):
        return f"{self._title} ({self._genre}, {self._year}) by {self._director}"

    # Getters and setters for encapsulation of attributes

    def get_title(self):
        """Returns the movie title."""
        return self._title

    def set_title(self, value):
        """Sets the movie title."""
        self._title = value

    def get_director(self):
        """Returns the movie director."""
        return self._director

    def set_director(self, value):
        """Sets the movie director."""
        self._director = value

    def get_genre(self):
        """Returns the movie genre."""
        return self._genre

    def set_genre(self, value):
        """Sets the movie genre."""
        self._genre = value

    def get_year(self):
        """Returns the movie's release year."""
        return self._year

    def set_year(self, value):
        """Sets the movie's release year."""
        self._year = value