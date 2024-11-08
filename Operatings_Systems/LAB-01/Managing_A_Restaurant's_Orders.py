from queue import deque
def RR_scheduling(orders, time_quantum):
    q = deque(orders)
    total_time = 0
    while q:
        current_order = q.popleft()
        if current_order > time_quantum:
            total_time += time_quantum
            q.append(current_order - time_quantum)
        else:
            total_time += current_order
    return f"The total time required to complete all orders is: {total_time} minutes (RR)"

orders = list(map(int,input("Enter Orders : ").split(",")))
time_quantum = int(input("Enter Quantum_time : "))
print(RR_scheduling(orders,time_quantum))

def fcfs_scheduling(orders):
    total_time = 0
    current_time = 0
    for order in orders:
        if current_time < total_time:
            current_time = total_time
        current_time += order
        total_time = current_time
    return f"The total time required to complete all orders is: {total_time} minutes (FCFS)"
print(fcfs_scheduling(orders))


def sjf_scheduling(orders):
    orders_sorted = sorted(orders)  
    total_time = 0
    current_time = 0
    for order in orders_sorted:
        if current_time < total_time:
            current_time = total_time
        current_time += order
        total_time = current_time
    return f"The total time required to complete all orders is: {total_time} minutes (SJF)"
print(sjf_scheduling(orders))


def priority_scheduling(orders, priorities):
    combined = list(zip(orders, priorities))
    combined_sorted = sorted(combined, key=lambda x: (x[1], x[0]))
    total_time = 0
    current_time = 0
    for order, priority in combined_sorted:
        if current_time < total_time:
            current_time = total_time
        current_time += order
        total_time = current_time
    return f"The total time required to complete all orders is: {total_time} minutes (Priority)"
print("----Enter Priorities----")
priorities = list(map(int, input().split(",")))
print(priority_scheduling(orders, priorities)) 

# 5,3,8,6
# 4
# for priority 
