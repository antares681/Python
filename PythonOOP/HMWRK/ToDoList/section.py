from Ex_01_Wild_Cat.task import Task

class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = list()

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        task_list = list(filter(lambda t: t.name == task_name, self.tasks))
        if task_list:
            task = task_list[0]
            task.cmpltd = True
            return f"Completed task {task.name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        compltd_tasks = list(filter(lambda t: t.cmpltd, self.tasks))
        # compltd_tasks = [task for task in self.tasks if task.completed]
        for ct in compltd_tasks:
            self.tasks.remove(ct)
        return f"Cleared {len(compltd_tasks)} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        for task in self.tasks:
            result += task.details()+"\n"
        return result