class BinarySearchTree:

    class Node:

        def __init__(self,task,leftNode,rightNode):
            self.taskArray = []
            self.leftNode = None
            self.rightNode = None

        def __str__(self):
            taskArray = []
            for task in self.taskArray :
                taskArray = taskArray + "\n" + str(task)
            return taskArray

    def __init__(self):
        self.firstNode = None
        print("Initing Binary Search Tree")

    def addNode(self,node):
        tree = self.firstNode
        if tree == None:
            tree = node
        else:
            selectionInsert(node,tree)

        def selectionInsert(node,tree):
            if len(tree.taskArray[0]) > 0 and tree.taskArray[0].priority > node.priority:
                print("Add node right when there are no nodes")
                return transverseTree(node,tree.leftNode)
            elif len(tree.taskArray[0]) > 0 and tree.priority < node.priority :
                print("Add Node left when there are no nodes")
                return transverseTree(node,tree.rightNode)
            elif len(tree.taskArray[0]) == 0 and tree.priority == node.priority:
                tree.taskArray.append(node)
                print("Add node when you find the right priority")

    def printTree(self):
        tree = self.firstNode
        transverseTree(tree)

        def transverseTree(tree):
            transverseTree(tree.leftNode)
            if len(tree.task) > 1:
                print(tree.task)
            transverseTree(tree.rightNode)
