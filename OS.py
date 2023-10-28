
def calculate_turnaround_time(processes, arrival_time, burst_time):
    n = len(processes)
    completion_time = [0] * n
    turnaround_time = [0] * n

    # Sort processes by burst time
    sorted_processes = sorted(range(n), key=lambda x: burst_time[x])

    current_time = 0
    for i in range(n):
        process_index = sorted_processes[i]
        current_time += burst_time[process_index]
        completion_time[process_index] = current_time

    for i in range(n):
        turnaround_time[i] = completion_time[i] - arrival_time[i]

    return turnaround_time

def calculate_waiting_time(processes, arrival_time, burst_time):
    n = len(processes)
    remaining_time = burst_time.copy()
    waiting_time = [0] * n

    current_time = 0
    while True:
        min_remain_time = float("inf")
        process_to_execute = None
        all_processes_completed = True

        for i in range(n):
            if arrival_time[i] <= current_time and remaining_time[i] < min_remain_time and remaining_time[i] > 0:
                min_remain_time = remaining_time[i]
                process_to_execute = i
                all_processes_completed = False

        if all_processes_completed:
            break

        remaining_time[process_to_execute] -= 1
        current_time += 1

        for i in range(n):
            if i != process_to_execute and arrival_time[i] <= current_time:
                waiting_time[i] += 1

    return waiting_time

def findWaitingTime(processes, n, wt):
    rt = [0] * n

    # Copy the burst time into rt[]
    for i in range(n):
        rt[i] = processes[i][1]
    complete = 0
    t = 0
    minm = 999999999
    short = 0
    check = False

    # Process until all processes get completed
    while complete != n:

        # Find the process with the minimum remaining time
        for j in range(n):
            if processes[j][2] <= t and rt[j] < minm and rt[j] > 0:
                minm = rt[j]
                short = j
                check = True
        if not check:
            t += 1
            continue

        # Reduce remaining time by one
        rt[short] -= 1

        # Update minimum
        minm = rt[short]
        if minm == 0:
            minm = 999999999

        # If a process gets completely executed
        if rt[short] == 0:

            # Increment complete
            complete += 1
            check = False

            # Find finish time of the current process
            fint = t + 1

            # Calculate waiting time
            wt[short] = fint - processes[short][1] - processes[short][2]

            if wt[short] < 0:
                wt[short] = 0

        # Increment time
        t += 1

def findWaitingTimeRobin(processes, n, bt, quantum):
    remaining_time = bt.copy()
    waiting_time = [0] * n
    t = 0  # Current time

    while True:
        done = True

        for i in range(n):
            if remaining_time[i] > 0:
                done = False

                if remaining_time[i] > quantum:
                    t += quantum
                    remaining_time[i] -= quantum
                else:
                    t += remaining_time[i]
                    waiting_time[i] = t - bt[i]
                    remaining_time[i] = 0

        if done:
            break

def findAverageWaitingTimeRobin(processes, n, bt, quantum):
    waiting_time = [0] * n
    findWaitingTimeRobin(processes, n, bt, quantum)
    return sum(waiting_time) / n

if __name__ == "__main__":
    processes = ["P1", "P2", "P3", "P4"]
    arrival_time = [0, 1, 2, 3]
    burst_time = [6, 2, 8, 3]

    turnaround_times = calculate_turnaround_time(processes, arrival_time, burst_time)

    # Calculate and print the average turnaround time
    average_turnaround_time = sum(turnaround_times) / len(turnaround_times)
    print("Average Turnaround Time (SRTF):", average_turnaround_time)

    waiting_times = calculate_waiting_time(processes, arrival_time, burst_time)

    # Calculate and print the average waiting time
    average_waiting_time = sum(waiting_times) / len(waiting_times)
    print("Average Waiting Time (SRTF):", average_waiting_time)

#--------------------------------------------------------------------------------------------------
    processes = [("P1", 6, 0), ("P2", 2, 1), ("P3", 8, 2), ("P4", 3, 3)]
    n = len(processes)
    waiting_times = [0] * n

    # Calculate waiting times
    findWaitingTime(processes, n, waiting_times)

    # Calculate and print the average waiting time
    average_waiting_time = sum(waiting_times) / n
    print("Average Waiting Time:", average_waiting_time)
    
    #---------------------------------------------------------------------
    processes = ["P1", "P2", "P3", "P4"]
    burst_time = [6, 2, 8, 3]
    quantum = 2

    average_waiting_time = findAverageWaitingTimeRobin(processes, len(processes), burst_time, quantum)
    print("Average Waiting Time (Round Robin):", average_waiting_time)
# def findWaitingTime(processes, n, wt):
#     rt = [0] * n

#     # Copy the burst time into rt[]
#     for i in range(n):
#         rt[i] = processes[i][1]
#     complete = 0
#     t = 0
#     minm = 999999999
#     short = 0
#     check = False

#     # Process until all processes get completed
#     while complete != n:

#         # Find the process with the minimum remaining time
#         for j in range(n):
#             if processes[j][2] <= t and rt[j] < minm and rt[j] > 0:
#                 minm = rt[j]
#                 short = j
#                 check = True
#         if not check:
#             t += 1
#             continue

#         # Reduce remaining time by one
#         rt[short] -= 1

#         # Update minimum
#         minm = rt[short]
#         if minm == 0:
#             minm = 999999999

#         # If a process gets completely executed
#         if rt[short] == 0:

#             # Increment complete
#             complete += 1
#             check = False

#             # Find finish time of the current process
#             fint = t + 1

#             # Calculate waiting time
#             wt[short] = fint - processes[short][1] - processes[short][2]

#             if wt[short] < 0:
#                 wt[short] = 0

#         # Increment time
#         t += 1

# # Define the process details
# processes = [("P1", 6, 0), ("P2", 2, 1), ("P3", 8, 2), ("P4", 3, 3)]
# n = len(processes)
# waiting_times = [0] * n

# # Calculate waiting times
# findWaitingTime(processes, n, waiting_times)

# # Calculate and print the average waiting time
# average_waiting_time = sum(waiting_times) / n
# print("Average Waiting Time:", average_waiting_time)