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
            index = self.__binarySearchIndex(task.get_priority(),self.taskArray, lambda task: task.get_priority())
            self.taskArray.insert(index,task)

    def __binarySearchIndex(self,value,array,accessMethod):
        middle = (len(self.taskArray) / 2) if ((len(self.taskArray) % 2) == 0) else (len(self.taskArray) // 2) + 1
        if len(array) <= 1:
            return 0
        else:
            middle = int(middle)
        if value == accessMethod(array[middle]):
            return middle
        elif value < accessMethod(array[middle]):
            print(array[:middle])
            return middle + self.__binarySearchIndex(value,array[:middle],accessMethod)
        else:
            return middle - self.__binarySearchIndex(value,array[middle:],accessMethod)

    def __str__(self):
        taskString = ""
        for task in self.taskArray:
            taskString = taskString + str(task) + " \n"
        return taskString
