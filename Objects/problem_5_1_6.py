

class TodoItem:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed
    
    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description
    
    def getCompleted(self):
        return self.completed
    
    
    def setTitle(self, title):
        if type(title) == str:
            self.title = title
        else:
            self.title = None

    def setDescription(self, description):
        if type(description) == str:
            self.description = description
        else:
            self.description = None

    def setCompleted(self, completed):
        if type(completed) == bool:
            self.completed = completed
        else:
            self.completed = None
        
#Below are some lines of code that will test your class.
#You can change this code to test how your class behaves
#with different variables and method calls.
#

item = TodoItem("Mow", "Mow the lawn")
print(item.getTitle())
print(item.getDescription())
print(item.getCompleted())
item.setCompleted(True)
print(item.getCompleted())
item.setTitle(False)
print(item.getTitle())


