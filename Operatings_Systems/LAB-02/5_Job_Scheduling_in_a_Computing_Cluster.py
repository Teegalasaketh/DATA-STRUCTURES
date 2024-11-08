from queue import Queue
def calculate_time(h_priority,m_priority,l_priority):
    total_time = 0
    q = Queue()
    for j,t in h_priority.items():
        q.put(t)
    for j, t in m_priority.items():
        q.put(t)
    for j,t in l_priority.items():
        q.put(t)
    while not q.empty():
        total_time += int(q.get())
    return f"The total time required to complete all jobs is: {total_time} units"
#n = 3
h_priority = {"Job A" : 20 , "Job B" : 15 ,"Job C" : 25}
m_priority = {"Job D" : 10 , "Job E" : 12 ,"Job F" : 8}
l_priority = {"Job G" : 5 , "Job H" : 4 ,"Job I" : 6}
""" print("---High Priority(Critical) Jobs---")
for i in range(n):
    x = input("Enter job : ")
    y = input("Enter Value : ")
    h_priority[x] = y
print("---Medium Priority(Standard) Jobs---")
for i in range(n):
    x = input("Enter job : ")
    y = input("Enter Value : ")
    m_priority[x] = y
print("---Low Priority(Background) Jobs---")
for j in range(n):
    x = input("Enter job : ")
    y = input("Enter Value : ")
    l_priority[x] = y """
print(calculate_time(h_priority,m_priority,l_priority)) 


""" 
A : 20 units
B : 15 units
C : 25 units
-----------------
D : 10 units
E : 12 units
F : 8 units 
------------------
G : 5 units 
H : 4 units 
I : 6 units 
"""