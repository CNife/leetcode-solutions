"""
1670. 设计前中后队列
https://leetcode.cn/problems/design-front-middle-back-queue
"""
from collections import deque


class FrontMiddleBackQueue:
    def __init__(self):
        self.left: deque[int] = deque()
        self.right: deque[int] = deque()

    def pushFront(self, value: int) -> None:
        self.left.appendleft(value)
        self.balance()

    def pushMiddle(self, value: int) -> None:
        match len(self.left) - len(self.right):
            case 0:
                self.right.appendleft(value)
            case -1:
                self.left.append(value)
            case _:
                raise RuntimeError("unreachable")

    def pushBack(self, value: int) -> None:
        self.right.append(value)
        self.balance()

    def popFront(self) -> int:
        if self.left:
            value = self.left.popleft()
        elif self.right:
            value = self.right.popleft()
        else:
            return -1
        self.balance()
        return value

    def popMiddle(self) -> int:
        match len(self.left) - len(self.right):
            case 0:
                if self.left:
                    return self.left.pop()
                return -1
            case -1:
                return self.right.popleft()
            case _:
                raise RuntimeError("unreachable")

    def popBack(self) -> int:
        if self.right:
            value = self.right.pop()
            self.balance()
            return value
        return -1

    def balance(self):
        if (len_diff := len(self.left) - len(self.right)) < -1:
            self.left.append(self.right.popleft())
        elif len_diff > 0:
            self.right.appendleft(self.left.pop())


if __name__ == "__main__":
    queue = FrontMiddleBackQueue()
    queue.pushFront(1)
    queue.pushBack(2)
    queue.pushMiddle(3)
    queue.pushMiddle(4)
    assert queue.popFront() == 1
    assert queue.popMiddle() == 3
    assert queue.popMiddle() == 4
    assert queue.popBack() == 2
    assert queue.popFront() == -1
