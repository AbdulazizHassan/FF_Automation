import random
import time

agents = ["Louis Young", "Kai Bennet", "Lamar Davis", "Rama Olivia"]

call_queue = []

agent_breaks = {agent: False for agent in agents}
def receive_calls():
    for call_id in range(1, 11):
        print(f"Incoming call {call_id} added to queue.")
        call_queue.append(f"Call {call_id}")
        time.sleep(1)
        
def assign_calls():
    call_count = {agent: 0 for agent in agents}
    max_calls_before_break = 3
    max_agents_on_break = 1

    while call_queue:
        available_agents = [agent for agent, on_break in agent_breaks.items() if not on_break]
        if available_agents:
            call = call_queue.pop(0)
            agent = random.choice(available_agents)
            print(f"{call} assigned to {agent}.")
            call_count[agent] += 1
            time.sleep(2)

            if call_count[agent] >= max_calls_before_break:
                agents_on_break = sum(agent_breaks.values())
                if agents_on_break < max_agents_on_break:
                    print(f"{agent} is going on a break.")
                    agent_breaks[agent] = True
                    time.sleep(5)
                    print(f"{agent} is back from break.")
                    agent_breaks[agent] = False
                    call_count[agent] = 0
        else:
            print("No available agents. Waiting...")
            time.sleep(2)

def main():
    print("Starting call center automation with break assignment...\n")
    receive_calls()
    assign_calls()
    print("All calls have been handled.")

main()
