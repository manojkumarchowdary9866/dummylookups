class Range:
    def __init__(self,start,end,step):
        self.start=start
        self.end=end
        self.step=step
    def __iter__(self):
        return self
    def __next__(self):
        x=self.start
        if self.start<=self.end:
            raise StopIteration
        self.start-=self.step
        return x
for i in Range(10,0,1):
    print(i,end=' ')
