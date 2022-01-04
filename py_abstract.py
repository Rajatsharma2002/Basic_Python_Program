from abc import ABC , abstractmethod

class shape(ABC):
    @abstractmethod
    def print(self):
        return 0

class square(shape):
    side=6
    def print(self):
        return self.side*self.side

class rectangle(shape):
    length=6
    breadth=8
    height=5
    def print(self):
        return self.length*self.breadth*self.height

s=square()
r=rectangle()
print(s.print())
print(r.print())