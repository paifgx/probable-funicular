def get_description(item) -> str:
    return item.description()

class Book:
    def description(self) -> str:
        return "This is a book."

class Movie:
    def description(self) -> str:
        return "This is a movie."


book = Book()
movie = Movie()

print(get_description(book))
print(get_description(movie))

def call_description(item):
    if hasattr(item, "description"):
        return item.description()
    return "No description available."

# isinstance(obj, class)
# hasattr(obj, "methode_name")