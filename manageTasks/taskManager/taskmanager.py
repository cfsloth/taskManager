from binarySearchTree import BinarySearchTree

class TaskManager(object):
    """docstring forTaskManager."""

    def __init__(self):
        self.binarySearchTree = BinarySearchTree()
        print("Initing TaskManager")
        print("Initializing the BinaryBalanceTree")

    """Adding task ordered by priority"""
    """Maibe adding a check for autheticity of the object """
    def addTask(self,task):
        print("Add Task")
        self.binarySearchTree.addTask(task)

    def __str__(self):
        print(self.binarySearchTree.printTree())
