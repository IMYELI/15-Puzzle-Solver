class PrioQueue:
    def __init__(self):
        self.Queue = []
        self.length = 0

    def enqueue(self, Puzzle):
        if(self.length == 0):
            self.Queue.insert(0,Puzzle)
        else:
            i = 0
            while(i<self.length and Puzzle[0]>self.Queue[i][0]):
                i += 1    
            self.Queue.insert(i,Puzzle)
        self.length += 1
    
    def dequeue(self):
        if(self.length == 0):
            print("Queue kosong")
        self.length -= 1
        return self.Queue.pop(0)
        
                