class Task:
    def __init__(self, title:str, summary:str, isAnAssignment:bool):
        self.title = title
        self.summary = summary
        self.isAnAssignment = isAnAssignment

myTask = Task('my task', 'do the things', False)
print(myTask.isAnAssignment) 