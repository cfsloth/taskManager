from task import Task

class TaskManager(object):
    """docstring forTaskManager."""

    def __init__(self):
        print("Initing TaskManager")
        self.taskArray = []

    """Adding task ordered by priority"""
    """Maibe adding a check for autheticity of the object """
    def addTask(self,task):
        if len(self.taskArray) == 0 or self.taskArray[0].get_priority() <= task.get_priority():
            self.taskArray.insert(0,task)
        else:
            index = self.__binarySearchIndex(task.get_priority,self.taskArray,'get_priority')
            self.taskArray.insert(index,task)

    def __binarySearchIndex(self,value,array,acessMethod):
        middle = 0
        if len(self.taskArray) > 0:
            middle = (len(self.taskArray) / 2)
        if value == array[int(middle)].acessMethod():
            return middle
        elif value < array[int(middle)].acessMethod():
            self.__binarySearchIndex(value,array[:middle])
        else:
            self.__binarySearchIndex(value,array[middle:])

    def __str__(self):
        taskString = ""
        for task in self.taskArray:
            taskString = taskString + str(task) + " \n"
        return taskString
