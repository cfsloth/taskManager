class Task:

    def __init__(self,id,name,category="",priority=1):
        self.id = id
        self.name = name
        self.category = category
        self.priority = priority
        self.concluded = False
        self.active_days = 0
        print("Beggining Class")

    def get_priority(self):
        return self.priority

    def set_priority(self,priority):
        self.priority = priority

    def __str__(self):
        return str(self.id) + " | " + self.name + " | " + self.category + " | " + str(self.priority) + " | "
