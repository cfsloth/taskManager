class Node:

    def __init__(self):
        self.rightNode = None
        self.leftNode = None
        self.taskArray = []

    def addToArray(self,task):
        self.taskArray.append(task)

    def __str__(self):
        print("Array:", str(self.taskArray) ,"\n")
