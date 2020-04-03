class BinarySearchTree:

    def __init__(self):
        self.binarySearchTree = None
        print("Initing Binary Search Tree")

    def addTask(self,task):
        def innerAddTask(treeNode,task):
            if self.binarySearchTree != None:
                if task.priority < self.treeNode.taskArray[0].priority:
                    return self.addTask(treeNode.leftNode,task)
                elif task.priority > self.treeNode.taskArray[0].priority:
                    return self.addTask(treeNode.rightNode,task)
                else:
                    treeNode.addToArray(task)
            else:
                self.treeNode = self.Node().addToArray(task)
                print("Task added with success")

        innerAddTask(self.binarySearchTree,task)

    def printTree(self):
        def innerPrint(node):
            print(node)
            return innerPrint(node.rightNode) + innerPrint(node.leftNode)
        innerPrint(self.binarySearchTree)

    class Node(object):

        def __init__(self):
            self.rightNode = None
            self.leftNode = None
            self.taskArray = []

        def addToArray(self,task):
            self.taskArray.append(task)

        def __str__(self):
            printf(Node.taskArray)
