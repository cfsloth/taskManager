from task import Task

"""Using a array for simple purpose. Using other DS later for speed purposes"""
class TaskManager(object):
    """docstring forTaskManager."""

    def __init__(self):
        print("Initing TaskManager")
        self.taskArray = []

    def addTask(task):
        if self.taskArray == None or self.taskArray[0].get_priority() <= task.get_priority():
            self.taskArray.insert(0,task)
        else:
            index = binarySearchIndex(task.get_priority,self.taskArray,get_priority())
            self.taskArray.insert(index,task)

    def __binarySearchIndex(value,array,acessMethod):
        middle = (len(self.taskArray) / 2) if ((len(self.taskArray) / 2) % 0) else (len(self.taskArray) / 2) + 1
        if value == array[middle].acessMethod:
            return middle
        else if value < array[middle].acessMethod:
            binarySearchIndex(value,array[:middle])
        else:
            binarySearchIndex(value,array[middle:])

    def removeTask(identificator):



t = Task("Learn Proggramming")
print(t)
