import test
import pytest

def test_get_description():
    book = test.Book()
    movie = test.Movie()
    
    assert test.get_description(book) == "This is a book."
    assert test.get_description(movie) == "This is a movie."