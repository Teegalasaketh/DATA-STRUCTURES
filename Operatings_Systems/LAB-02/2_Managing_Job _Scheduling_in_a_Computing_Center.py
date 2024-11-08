from queue import Queue
def calculate_total_time(h_priority,l_priority):
    total_time = 0
    q = Queue()
    for i, j in h_priority.items():
        q.put((i, j))
    for i, j in l_priority.items():
        q.put((i, j))
    while not q.empty():
        job, time = q.get()
        total_time += int(time)
    return f"Total time to complete all jobs: {total_time} units"
#n = 3
h_priority = {"Job A" : 8 , "Job B" : 5 ,"Job C" : 10}
l_priority = {"Job D" : 6 , "Job E" : 3 ,"Job F" : 7}
""" print("---High Priority Jobs(System)---")
for i in range(n):
    x = input("Enter job : ")
    y = input("Enter Value : ")
    h_priority[x] = y
print("---Low Priority Jobs(User)---")
for j in range(n):
    x = input("Enter job : ")
    y = input("Enter Value : ")
    l_priority[x] = y """
print(calculate_total_time(h_priority,l_priority)) 



""" 
A : 8 units
B : 5 units
C : 10 units
-------------------
D : 6 units
E : 3 units
F : 7 units """
