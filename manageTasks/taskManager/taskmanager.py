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
        self.binarySearchTree.addNode(task)
        print("Task added with success")

    def __str__(self):
        print(self.binarySearchTree.printTree())
