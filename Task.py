class Task:
    def __init__(title, summary, dueDate, isAnAssignment):
        self.title = title
        self.summary = summary
        self.dueDate = dueDate
        self.isAnAssignment = isAnAssignment

myTask = Task('my task', 'do the things', 'tomorrow', false)
print(myTask.title) 