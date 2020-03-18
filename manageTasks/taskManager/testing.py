from task import Task
from taskmanager import TaskManager

t = Task(1,"TODO: Learn something",priority=3)
t2 = Task(2,"TODO: Check bugs on a program",priority=1)
t3 = Task(3,"TODO: Check for priority algorithm",priority=7)
t4 = Task(4,"TODO: Talk to GIrlfriend",priority=3)
t5 = Task(5,"TODO: Check covid-19 status",priority=2)
t6 = Task(6,"TODO: Check algorithms updates",priority=10)
task_manager = TaskManager()
task_manager.addTask(t)
task_manager.addTask(t2)
task_manager.addTask(t3)
task_manager.addTask(t4)
task_manager.addTask(t5)
task_manager.addTask(t6)
print(task_manager)

"""Removing task"""
