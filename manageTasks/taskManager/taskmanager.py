from binarySearchTree import BinarySearchTree

class TaskManager(object):
    """docstring forTaskManager."""

    class Node(object):

        def __init__(self):
            self.rightNode = None
            self.leftNode = None
            self.taskArray = None

        def addToArray(task):
            self.taskArray.append(task)

    def __init__(self):
        self.binarySearchTree = BinarySearchTree()
        print("Initing TaskManager")
        print("Initializing the BinaryBalanceTree")

    """Adding task ordered by priority"""
    """Maibe adding a check for autheticity of the object """
    def addTask(self,task
        def innerAddTask(treeNode,task):
            if treeNode != None:
                if task.priority < treeNode.taskArray[0].priority:
                    self.addTask(treeNode.leftNode,task)
                elif task.priority > treeNode.taskArray[0].priority:
                    self.addTask(treeNode.rightNode,task)
                else:
                    treeNode.addToArray(task)
            else:
                treeNode = Node().addToArray(task)
                print("Task added with success")

        innerAddTask(self.treeNode,task)
    def __str__(self):
        print(self.binarySearchTree.printTree())
