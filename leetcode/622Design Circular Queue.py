
class MyCircularQueue(object):

    def __init__(self, k: int):
        """
        :type k: int
        """
        self.thelist = [None for i in range(k)]
        self.max = k
        self.where_front = 0
        self.where_rear = 0



    def enQueue(self, value: int) -> bool:
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.thelist[self.where_rear] = value
        self.where_rear = (self.where_rear + 1) % self.max
        return True

    def deQueue(self) -> bool:
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.thelist[self.where_front] = None
        self.where_front = (self.where_front + 1) % self.max
        return True

    def Front(self) -> int:
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.thelist[self.where_front]

    def Rear(self) -> int:
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.thelist[self.where_rear - 1]


    def isEmpty(self) -> bool:
        """
        :rtype: bool
        """
        for i in range(self.max):
            if self.thelist[i] is not None:
                return False
        return True

    def isFull(self) -> bool:
        """
        :rtype: bool
        """
        for i in range(self.max):
            if self.thelist[i] is None:
                return False
        return True


