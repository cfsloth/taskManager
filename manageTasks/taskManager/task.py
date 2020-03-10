class Task:
    
    def __init__(self,id,name,category="",priority=1):
        self.id = id
        self.name = name
        self.category = category
        self.priority = priority
        self.concluded = False
        self.active_days = 0
        print("Beggining Class")

    def get_name():
        return self.name

    def get_category():
        return self.category

    def get_priority():
        return self.priority

    def set_name(name):
        self.name = name

    def set_category(category):
        self.category = category

    def set_priority(priority):
        self.priority = priority

    def __str__(self):
        return str(self.id) + " | " + self.name + " | " + self.category + " | " + str(self.priority) + " | "  
