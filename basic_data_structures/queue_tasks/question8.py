from queue import Queue
from deque import Deque
import random

class Car(object):
    """
      tests have not been though out yet.
    """
    def __init__(self, num, current_time):
        self.arrive_time = current_time
        self.num = num

    def get_arrive_time(self):
        return self.arrive_time

    def get_car_num(self):
        return self.num

class CarWash(object):
    def __init__(self):
        self.arrivals = Queue()
        self.wait_times = []
        self.car_count = 1
        self.busy = False

    def add_car(self, current_time):
        self.arrivals.enqueue(Car(self.car_count, current_time))
        self.car_count += 1

    def wash_car(self, current_time):
        wc = self.arrivals.deque()
        self.add_wait_time(current_time, wc.get_arrive_time())
        self.busy = True

    def add_wait_time(self, current_time, arrive_time):
        self.wait_times.append(current_time - arrive_time)

    def isCarWashBusy(self):
        return self.busy

    def clearCarWash(self):
        if self.car_wash_timer == 25:
            self.busy = False
            self.car_wash_timer = 1
        self.car_wash_timer += 1

    def waiting_to_wash(self):
        return self.arrivals.size()

def random_arrival(arrival_num):
    chance = random.randrange(1, arrival_num + 1)
    return chance == 10

def car_wash_simulation(time):
    c = CarWash()
    current_time = 0
    while current_time < time:
        current_time += 1
        if random_arrival(10):
            c.add_car(current_time)
        if c.waiting_to_wash() > 0:
            if not c.isCarWashBust():
                c.wash_car(current_time)
            else:
                c.clearCarWash()
        return c.wait_times, c.waiting_to_wash()

def average(num_list):
    return float(sum(num_list)) / len(num_list)



if __name__ == '__main__':
    import doctest
    doctest.testmod()

