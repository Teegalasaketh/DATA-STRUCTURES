from queue import Queue
def calculate_time(h_priority,l_priority):
    total_time = 0
    q = Queue()
    for j,t in h_priority.items():
        q.put(t)
    for j,t in l_priority.items():
        q.put(t)
    while not q.empty():
        total_time += int(q.get())
    return f"The total time required to complete all print jobs is: {total_time} units"
#n = 3
h_priority = {"Job A" : 15 , "Job B" : 10 ,"Job C" : 20}
l_priority = {"Job D" : 5 , "Job E" : 8 ,"Job F" : 3}
""" print("---High Priority Jobs---")
for i in range(n):
    x = input("Enter job : ")
    y = input("Enter Value : ")
    h_priority[x] = y
print("---Low Priority Jobs---")
for j in range(n):
    x = input("Enter job : ")
    y = input("Enter Value : ")
    l_priority[x] = y """
print(calculate_time(h_priority,l_priority)) 


""" 
A : 15 units
B : 10 units
C : 20 units
---------------------
D : 5 units
E : 8 units
F : 3 units """