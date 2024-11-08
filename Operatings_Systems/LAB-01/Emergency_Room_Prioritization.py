from queue import PriorityQueue,deque
def priority_scheduling(patients):
    pq = PriorityQueue()
    total_time = 0
    for p in patients:
        pq.put(p)
    while not pq.empty():
        priority, treatment_time = pq.get()
        total_time += treatment_time
    return f"The total time required to treat all patients is: {total_time} minutes (Priority)"

n, m = 4,4
print("-------Enter Patients With Priorites(only Four)------")
if n == m:
    patients = []
    for i in range(n):
        p = [int(x) for x in input().split(',')]
        if len(p) == 2:  
            patients.append(tuple(p))
        else:
            print("Invalid input format. Each entry must have exactly two numbers separated by a comma.")
            break
    else:
        print(priority_scheduling(patients))
else:
    print("The number of patients must match the number of entries.")



def fcfs_scheduling(patients):
    total_time = 0
    current_time = 0
    for _, treatment_time in patients:
        if current_time < total_time:
            current_time = total_time
        current_time += treatment_time
        total_time = current_time
    return f"The total time required to treat all patients is: {total_time} minutes (FCFS)"
print(fcfs_scheduling(patients))



def rr_scheduling(patients, time_quantum):
    q = deque(patients)
    total_time = 0
    while q:
        priority, treatment_time = q.popleft()
        if treatment_time > time_quantum:
            total_time += time_quantum
            q.append((priority, treatment_time - time_quantum))
        else:
            total_time += treatment_time
    return f"The total time required to treat all patients is: {total_time} minutes (RR)"
time_quantum = 4
print(rr_scheduling(patients, time_quantum))


def sjf_scheduling(patients):
    patients_sorted = sorted(patients, key=lambda x: x[1])
    total_time = 0
    current_time = 0
    for _, treatment_time in patients_sorted:
        if current_time < total_time:
            current_time = total_time
        current_time += treatment_time
        total_time = current_time
    return f"The total time required to treat all patients is: {total_time} minutes (SJF)"
print(sjf_scheduling(patients)) 

# 4 4
# 1,10
# 2,8
# 3,15
# 4,5
