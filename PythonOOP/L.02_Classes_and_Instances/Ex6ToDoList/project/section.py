from task import Task

class Section:
    def __init__(self, name:str):
        self.name = name
        self.tasks = []

    def add_task(self, task:Task):
        if self.name in self.tasks:
            return f"Task {Task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(task_name: str):
        if task_name in self.tasks:
            Task.complete_task = True
            return f"Completed task {Task.name}"
        else:
            return f"Could not find task with the name {Task.name}"

    def clean_section():
        return f"Cleared {amount of removed tasks} tasks."
    def view_section()
        return
        f "Section {section_name}:
        for el in self.tasks
        f'{details of the first task}

