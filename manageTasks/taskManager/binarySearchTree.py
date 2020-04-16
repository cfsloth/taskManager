from node import Node

class BinarySearchTree:

    def __init__(self):
        self.binaryTree = None
        print("Initing Binary Search Tree")

    def addTask(self,task):

        def innerAddTask(treeNode,task):
            if treeNode != None:
                if task.priority < treeNode.taskArray[0].priority:
                    if treeNode.leftNode != None:
                        return innerAddTask(treeNode.leftNode,task)
                    else:
                        treeNode.leftNode = Node().addToArray(task)
                        return 1
                elif task.priority > treeNode.taskArray[0].priority:
                    if treeNode.rightNode != None:
                        return innerAddTask(treeNode.rightNode,task)
                    else:
                        treeNode.rightNode = Node().addToArray(task)
                        return 1
                else:
                    #This case is when there are equals
                    treeNode.addToArray(task)
                    return 1
            else:
                print("First task added with success")
                new_node = Node()
                new_node.addToArray(task)
                self.binaryTree = new_node
                return 1

        innerAddTask(self.binaryTree,task)

    def printTree(self):
        def innerPrint(node):
            if node != None:
                print(node)
                return innerPrint(node.rightNode) + innerPrint(node.leftNode)
        innerPrint(self.binaryTree)
