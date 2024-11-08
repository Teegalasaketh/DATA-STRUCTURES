from queue import Queue
def calculate_total_time(system_processes, user_processes):
    total_time = 0
    q = Queue()
    for p,t in system_processes.items():
        q.put(t)
    for p,t in user_processes.items():
        q.put(t)
    while  not q.empty():
        total_time += int(q.get())
    return f'Total time required to complete all processes is : {total_time} units'
#n = 3
system_processes = {"Process A" : 5 , "Process B" : 3 ,"Process C" : 7}
user_processes = {"Process D" : 4 , "Process E" : 2 ,"Process F" : 6}
""" print("---System Processes---")
for i in range(n):
    x = input("Enter process : ")
    y = input("Enter Value : ")
    system_processes[x] = y
print("---User Processes---")
for j in range(n):
    x = input("Enter process : ")
    y = input("Enter Value : ")
    system_processes[x] = y """
print(calculate_total_time(system_processes,user_processes))


""" 
A : 5 units
B : 3 units
C : 7 units
----------------------------
D : 4 units
E : 2 units
F : 6 units """