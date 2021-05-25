# class Person:
#     def __init__(self, name, age, kg):
#         self.name = name
#         self.age = age
#         self.kg = kg
#
#
#
# person = Person("Test", 12, 30)
# person2 = Person("Lazar", 40, 100)


class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes

comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)
