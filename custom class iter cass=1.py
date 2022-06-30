class Range():
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        x=self.start
        return x
for i in Range(10,15):
    print(i)
