class BinarySearchTree:

    class Node:

        def __init__(self):
            self.rightNode = None
            self.leftNode = None
            self.taskArray = []

        def addToArray(self,task):
            self.taskArray.append(task)

        def __str__(self):
            print("Array:", Node.taskArray ,"\n")

    def __init__(self):
        self.binaryTree = None
        print("Initing Binary Search Tree")

    def addTask(self,task):
        def innerAddTask(treeNode,task):
            if self.binaryTree != None:
                if task.priority < self.treeNode.taskArray[0].priority:
                    print("goes left")
                    return self.addTask(treeNode.leftNode,task)
                elif task.priority > self.treeNode.taskArray[0].priority:
                    print("goes right")
                    return self.addTask(treeNode.rightNode,task)
                else:
                    treeNode.addToArray(task)
                    print("Task added with sucess")
                    return 1
            else:
                print("First task added with success")
                deb = self.Node().addToArray(task)
                treeNode = self.Node().addToArray(task)
                print(treeNode.taskArray)
                return 1

        innerAddTask(self.binaryTree,task)

    def printTree(self):
        def innerPrint(node):
            if node != None:
                print(node)
                return innerPrint(node.rightNode) + innerPrint(node.leftNode)
        innerPrint(self.binarySearchTree)
