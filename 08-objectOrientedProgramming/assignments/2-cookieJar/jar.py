
import sys


class Jar:
    def __init__(self , capacity = 12,size = 0):

        if capacity < 0:
            raise ValueError()
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪" * self.size

    def deposit(self,n):
        if self.size + n > self.capacity:
            raise ValueError("Deposit Error")
        self.size += n


    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Withdraw Error")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,capacity):
        if capacity < 1:
            raise ValueError("capacity error")
        self._capacity = capacity


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,size):
        if size < 0 :
            raise ValueError("Size Error")
        self._size = size


def main():
    jar = Jar()
    print(jar)
    jar.deposit(3)
    print(jar)
    jar.withdraw(2)
    print(jar)

if __name__ == "__main__":
    main()
