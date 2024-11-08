def fcfs_scheduling(arrival_times, pages):
    n = len(arrival_times)
    current_time = 0
    total_time = 0
    for i in range(n):
        if current_time < arrival_times[i]:
            current_time = arrival_times[i]
        current_time += pages[i]
        total_time  = current_time
    return f'The total time taken to complete all printing tasks is: {total_time} seconds (FCFS)'
arrival_times = list(map(int,input("Enter Arrival_times :").split(',')))
pages = list(map(int,input("Enter Pages :").split(',')))
print(fcfs_scheduling(arrival_times,pages))


def sjf_scheduling(arrival_times, pages):
    jobs = sorted(zip(arrival_times, pages), key=lambda x: (x[0], x[1]))  
    current_time = 0
    total_time = 0
    
    for arrival_time, pages in jobs:
        if current_time < arrival_time:
            current_time = arrival_time
        current_time += pages
        total_time = current_time
        
    return f'The total time taken to complete all printing tasks is: {total_time} seconds (SJF)'

print(sjf_scheduling(arrival_times, pages))


from collections import deque
def rr_scheduling(arrival_times, pages, quantum_time):
    n = len(arrival_times)
    queue = deque([(arrival_times[i], pages[i]) for i in range(n)])  
    current_time = 0
    total_time = 0
    
    while queue:
        arrival_time, pages = queue.popleft()
        if current_time < arrival_time:
            current_time = arrival_time
        
        if pages > quantum_time:
            current_time += quantum_time
            queue.append((current_time, pages - quantum_time))
        else:
            current_time += pages
        total_time = current_time
    
    return f'The total time taken to complete all printing tasks is: {total_time} seconds (RR)'

quantum_time = int(input('Enter quantum_time: '))
print(rr_scheduling(arrival_times, pages, quantum_time))


def priority_scheduling(arrival_times, pages, priorities):
    n = len(arrival_times)
    jobs = sorted(zip(arrival_times, pages, priorities), key=lambda x: (x[0], x[2]))  
    current_time = 0
    total_time = 0
    
    for arrival_time, pages, priority in jobs:
        if current_time < arrival_time:
            current_time = arrival_time
        current_time += pages
        total_time = current_time
        
    return f'The total time taken to complete all printing tasks is: {total_time} seconds (Priority)'

print("----Enter Priorities----")
priorities = list(map(int,input().split(',')))
print(priority_scheduling(arrival_times, pages, priorities))

# 0,1,3,5
# 10,5,3,7