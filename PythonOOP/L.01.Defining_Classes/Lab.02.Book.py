class Book:
    def __init__(self, name, author, pages:int):
        self.name = name
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.name} {self.author} {self.pages}'

print(Book('Lazar', 'Galaxy', 8))


# class Book:
#     def __init__(self, name:str, author:str, pages:int):
#         self.name = name
#         self.author = author
#         self.pages = pages
