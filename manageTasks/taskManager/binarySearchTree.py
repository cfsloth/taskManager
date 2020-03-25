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
            if tree != None and len(tree.taskArray) > 0 and tree.taskArray[0].priority > node.priority:
                print("Add node right when there are no nodes")
                return transverseTree(node,tree.leftNode)
            elif tree != None and tree.priority < node.priority :
                print("Add Node left when there are no nodes")
                return transverseTree(node,tree.rightNode)
            elif len(tree.taskArray[0 :
                tree.append(node)

            else tree.priority == node.priority:
                tree.taskArray.append(node)

    def printTree(self):
        tree = self.tree
        if tree != None
