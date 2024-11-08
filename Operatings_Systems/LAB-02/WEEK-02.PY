from queue import Queue
n=int(input("Enter Function Number: "))
if(n==1):
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
    print("---------Function_01----------")
    print(calculate_total_time(system_processes,user_processes))
elif(n==2):
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
    h_priority = {"Job A" : 8 , "Job B" : 5 ,"Job C" : 10}
    l_priority = {"Job D" : 6 , "Job E" : 3 ,"Job F" : 7}
    print("---------Function_02----------")
    print(calculate_total_time(h_priority,l_priority)) 

elif(n==3):
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
    print("---------Function_03----------")
    h_priority = {"Job A" : 15 , "Job B" : 10 ,"Job C" : 20}
    l_priority = {"Job D" : 5 , "Job E" : 8 ,"Job F" : 3}
    print(calculate_time(h_priority,l_priority)) 

elif(n==4):
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
    h_priority = {"Task A" : 12 , "Task B" : 8 ,"Task C" : 15}
    l_priority = {"Task D" : 6 , "Task E" : 4 ,"Task F" : 10}
    print("---------Function_04----------")
    print(calculate_time(h_priority,l_priority)) 
elif(n==5):
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
    h_priority = {"Job A" : 20 , "Job B" : 15 ,"Job C" : 25}
    m_priority = {"Job D" : 10 , "Job E" : 12 ,"Job F" : 8}
    l_priority = {"Job G" : 5 , "Job H" : 4 ,"Job I" : 6}
    print("---------Function_05----------")
    print(calculate_time(h_priority,m_priority,l_priority)) 
else:
    print("Invalid Function number")