class BinarySearchTree:

    class Node:

        def __init__(self,task,leftNode,rightNode):
            self.task = task
            self.leftNode = None
            self.rightNode = None

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
            if tree.priority > node.priority and tree.leftNode == None:
                print("Add node right when there are no nodes")
                tree.leftNode = node
            elif tree.priority < node.priority and tree.rightNode == None:
                print("Add Node left when there are no nodes")
                tree.leftNode = node
            elif tree.priority == node.priority:
                print("Add node whenn you find the right priority")
            elif tree.priority => node.priority:
                return transverseTree(node,tree.leftNode)
            elif tree.priority < node.priority:
                return transverseTree(node,tree.rightNode)
