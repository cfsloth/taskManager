class TaskManager(object):
    """docstring forTaskManager."""

    def __init__(self):
        print("Initing TaskManager")
        print("Initializing the BinaryBalanceTree")

    """Adding task ordered by priority"""
    """Maibe adding a check for autheticity of the object """
    def addTask(self,task):
        print("Adding task to the BBT")

    def __str__(self):
        taskString = ""
        for task in self.taskArray:
            taskString = taskString + str(task) + " \n"
        return taskString
