import threading
import time
from queue import Queue, PriorityQueue
from copy import deepcopy

class PubSub(threading.Thread):
    def __init__(self, publishers: list):
        print("PubSub init")
        super().__init__()
        self.publishers = publishers
        self.subscribers = set()
        self.pq = PriorityQueue()  
        self.stop_event = threading.Event()
        self.start()

    def stop(self):
        self.stop_event.set()

    def is_stopped(self):
        return self.stop_event.is_set()

    def subscribe(self, subscriber):
        self.subscribers.add(subscriber)
        
    def publish(self, data2publish):
        for item in data2publish:
            try:
                item_copy = deepcopy(item)
                item_copy.subscribers = self.subscribers.copy()
                self.pq.put_nowait(item_copy)
            except Exception as e:
                print("Pubsub: publish: " + str(e))


    def get_data(self, subscriber):
        if subscriber not in self.subscribers:
            raise Exception("Pubsub: get_data: Invalid pubsub subscriber!")

        out_data = []
        n = self.pq.qsize()
        if n > 0:
            data2keep = []
            try:
                for _ in range(n):
                    item = self.pq.get_nowait()

                    if subscriber in item.subscribers:
                        out_data.append(item.copy())
                        item.subscribers.remove(subscriber)

                    if len(item.subscribers) != 0:
                        data2keep.append(item)
            except Exception as e:
                print("Pubsub: get_data: " + str(e))

            for item in data2keep:
                self.pq.put_nowait(item)

        return out_data


    def run(self):
        while not self.stop_event.is_set():
            data2publish = []
            for publisher in self.publishers:
                n = publisher.qsize()
                if n > 0:
                    try:
                        for _ in range(n):
                            item = publisher.get_nowait()
                            data2publish.append(item)
                    except Exception as e:
                        print("Pubsub: run: " + str(e))
                        continue
            if len(data2publish) > 0:
                self.publish(data2publish)

            time.sleep(0.1)


    