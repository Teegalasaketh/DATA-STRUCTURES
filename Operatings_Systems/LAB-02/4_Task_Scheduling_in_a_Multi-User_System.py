from queue import Queue
def calculate_time(h_priority,l_priority):
    total_time = 0
    q = Queue()
    for task,t in h_priority.items():
        q.put(t)
    for task,t in l_priority.items():
        q.put(t)
    while not q.empty():
        total_time += int(q.get())
    return f"The total time required to complete all tasks is: {total_time} units"
#n = 3
h_priority = {"Task A" : 12 , "Task B" : 8 ,"Task C" : 15}
l_priority = {"Task D" : 6 , "Task E" : 4 ,"Task F" : 10}
""" print("---High Priority Tasks(System)---")
for i in range(n):
    x = input("Enter task : ")
    y = input("Enter Value : ")
    h_priority[x] = y
print("---Low Priority Tasks(User)---")
for j in range(n):
    x = input("Enter task : ")
    y = input("Enter Value : ")
    l_priority[x] = y """
print(calculate_time(h_priority,l_priority)) 


""" 
A : 12 units
B : 8 units
C : 15 units
---------------------
D : 6 units
E : 4 units
F : 10 units """