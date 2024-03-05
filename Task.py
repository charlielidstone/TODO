import datetime
class Task:
    def getDetails(self):
        return f"Title: {self.title}\nSummary: {self.summary}\nDue Date: {self.dueDate}\nIs an Assignment: {self.isAnAssignment}"

        
    def __init__(self, title:str, summary:str = "", dueDate:datetime = None, isAnAssignment:bool = False):
        self.title = title
        self.summary = summary
        self.dueDate = dueDate
        self.isAnAssignment = isAnAssignment