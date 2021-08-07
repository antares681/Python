class Task:
    def __init__(self, name:str, due_date:str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name:str):
        self.name = new_name
        return self.name

    def change_due_date(self, new_date:str):
        self.due_date = new_date
        return self.due_date

    def add_comment(self, comment:str):
        self.comments.append(comment)

    def edit(self,comment_nmbr: int, new_comment:str):
        if comment_nmbr <= len(self.comments):
            self.comments.pop(comment_nmbr)
            self.comments.insert(comment_nmbr, new_comment)
        else:
            print(f'Cannot find comment')

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"