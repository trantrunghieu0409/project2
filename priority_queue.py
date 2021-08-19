# A simple implementation of Priority Queue
# using Queue.
class PriorityQueue(object):
    def __init__(self):
        self.queue = []
  
    #def __str__(self):
    #    return ' '.join([str(i) for i in self.queue])
  
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
  
    # for inserting an element in the queue
    def insert(self, data):
        try:
            i = [x[0] for x in self.queue].index(data[0])
            if self.queue[i][1] > data[1]:
                self.queue[i] = data
        except ValueError:
            self.queue.append(data)
  
    # for popping an element based on Priority
    def delete(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i][1] > self.queue[min][1]:
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            pass