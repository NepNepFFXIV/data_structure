import heapq
import itertools
'''
Priority Queue implementation with each task is unique
Sort stable: 2 tasks of the same priority will be returned in order they were added
Work for tasks that don't have default comparison order
Can update the priority of a task in queue
'''
class PriorityQueue:
    REMOVED = 'REMOVED'
    def __init__(self):
        self.queue = []
        self.counter = itertools.count()
        self.entry_finder = {}

    def put(self, task, priority):
        if task in self.entry_finder:
            self._remove_task(task)
        entry = [priority, next(self.counter), task]
        self.entry_finder[task] = entry
        heapq.heappush(self.queue, entry)

    def pop(self):
        while self.queue:
            _, _, task = heapq.heappop(self.queue)
            if task is not PriorityQueue.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('Pop from an empty Priority Queue')

    def _remove_task(self, task):
        entry = self.entry_finder.pop(task)
        entry[-1] = PriorityQueue.REMOVED

    def __str__(self):
        return str(self.queue)

if __name__=="__main__":
    queue = PriorityQueue()
    queue.put('a', 4)
    queue.put('b', 1)
    queue.put('c', 2)
    queue.put('a', 5)
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    # print(queue)