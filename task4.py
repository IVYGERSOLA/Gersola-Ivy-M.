class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear Published: {self.year_published}"

# Create three book objects
book1 = Book("365 Days", "Blanka Lipińska", 2018)
book2 = Book("Fifty Shades of Grey", "E.L. James", 2011)
book3 = Book("Me Before You", "Jojo Moyes", 2012)

# Display their details
print(book1.describe())
print("\n" + "-"*30 + "\n")
print(book2.describe())
print("\n" + "-"*30 + "\n")
print(book3.describe())
