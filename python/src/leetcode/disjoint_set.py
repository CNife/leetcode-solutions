from array import array


class DisjointSet:
    def __init__(self, size: int):
        self.size: int = size
        self.data: array = array("I", range(size))

    def find(self, x: int) -> int:
        if self.data[x] != x:
            self.data[x] = self.find(self.data[x])
        return self.data[x]

    def unite(self, x: int, y: int) -> None:
        self.data[self.find(x)] = self.find(y)
