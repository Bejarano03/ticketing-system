import queue
import time
import random

class Ticket():
    def __init__(self, number, timestamp) -> None:
        self.number = number
        self.timestamp = timestamp

def generate(num_tickets, ticketing_queue):
    for i in range(num_tickets):
        cur_ts = time.time()
        cur_ticket = Ticket(number=i, timestamp=cur_ts)
        print(f"ticket numbers {i}, timestamp: {cur_ts} ")
        ticketing_queue.put(cur_ticket)
        time.sleep(random.random() * 10)

def process_tickets(ticketing_queue):
    while not ticketing_queue.empty():
        cur_ticket = ticketing_queue.get()
        print(f"process: ticket number  {cur_ticket.number}, timestamp: {cur_ticket.timestamp} ")
        time.sleep(random.random())


def main():
    ticketing_queue = queue.Queue()

    generate(num_tickets=5, ticketing_queue=ticketing_queue)
    print(list(ticketing_queue.queue))
    process_tickets(ticketing_queue=ticketing_queue)

main()