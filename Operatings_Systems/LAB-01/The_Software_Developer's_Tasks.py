def sjf_scheduling(task_times):
    task_times.sort()  
    total_time = 0
    elapsed_time = 0
    for time in task_times:
        elapsed_time += time
        total_time = elapsed_time
    return f'The total time required to complete all tasks is: {total_time} hours (SJF)'
task_times = list(map(int,input("Enter task_times : ").split(',')))
print(sjf_scheduling(task_times))

def fcfs_scheduling(task_times):
    total_time = 0
    elapsed_time = 0
    
    for time in task_times:
        elapsed_time += time
        total_time = elapsed_time
    return f'The total time required to complete all tasks is: {total_time} hours (FCFS)'

print(fcfs_scheduling(task_times))


from queue import PriorityQueue,deque

def rr_scheduling(task_times, quantum):
    queue = deque(task_times)
    total_time = 0
    current_task = 0
    while queue:
        current_task = queue.popleft()
        if current_task > quantum:
            total_time += quantum
            queue.append(current_task - quantum)
        else:
            total_time += current_task
    return f'The total time required to complete all tasks is: {total_time} hours (RR)'

quantum = int(input("Enter quantum Time: ")) 
print(rr_scheduling(task_times, quantum)) 



def priority_scheduling(tasks):
    patients = tasks
    pq = PriorityQueue()
    total_time = 0
    for p in patients:
        pq.put(p)
    while not pq.empty():
        priority, treatment_time = pq.get()
        total_time += treatment_time
    return f'The total time required to complete all tasks is: {total_time} hours (Priority)'

#n,m = 4,4
tasks_list = [(1,5),(3,7),(2,3),(4,4)]
print(priority_scheduling(tasks_list)) 
""" if (n==m):
    for i in range(n):
        p = [int(x) for x in input().split(',')]
        if len(p) == 2:  
            tasks_list.append(tuple(p))
        else:
            print("Invalid input format. Each entry must have exactly two numbers separated by a comma.")
    print(priority_scheduling(tasks_list))
else:
    print ("Enter Same Size Both, To Get Priority Scheduling") """


# 3,5,7,4