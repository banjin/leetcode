#!/usr/bin/env python3
#coding:utf-8

class MycircularDeque:
    def __init__(self, k):
        self._queue = []
        self._length = k

    def insertFront(self, value):
        if len(self._queue) >= self._length:
            return False
        self._queue.insert(0, value)
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self._queue) >= self._length:
            return False
        self._queue.append(value)
        return True


    def deleteFront(self, value):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self._queue:
            return False
        del self._queue[0]
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self._queue:
            return False
        self._queue.pop()
        return True


    def getFront(self):
        """
        Get the front item from the deque.
        """
        if self._queue:
            return self._queue[0]
        else:
             return -1


    def getRear(self):
        """
        Get the last item from the deque.
        """
        if self._queue:
            return self._queue[-1]
        else:
            return -1


    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        """
        if not self._queue:
            return True
        else:
            return False

    def isFull(self):
        return [False, True][len(self._queue) == self._length]
