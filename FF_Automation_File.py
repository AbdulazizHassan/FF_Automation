# call center automation program

import random
import time
from threading import Thread

# agents:
agents = ["Louis Young", "Kai Bennet", "Lamar Davis", "Rama Olivia"]

# queue list
call_queue = []

# method that simulates incoming calls
def receive_calls():
    for call_id in range(1, 11):  # this will simulate 10 calls
        print(f"WATCH OUT THERES A CLIENT ON THE LINE WITH ID {call_id} ADDED TO THE QUEUE.")
        call_queue.append(f"Call {call_id}")
        time.sleep(1)  # this will simulate the delays between calls

# this function assigns calls to agents
def assign_calls():
    while True:
        if call_queue and agents:
            call = call_queue.pop(0)
            agent = random.choice(agents)
            print(f"{call} assigned to {agent}.")
            time.sleep(2)  # this is to simulate the waiting time between calls
        elif not call_queue:
            break

# main
def main():
    print("starting call center automation program broskisss\n")
    receiver_thread = Thread(target=receive_calls)
    assigner_thread = Thread(target=assign_calls)
    receiver_thread.start()
    assigner_thread.start()
    receiver_thread.join()
    assigner_thread.join()
    print("go home")

main()
