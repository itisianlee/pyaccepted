'''
# 堆中父节点i与子节点left、right的位置关系
parent = int((i-1) / 2)    # 取整
left = 2 * i + 1
right = 2 * i + 2
'''
class Array(object):
    def __init__(self, size = 32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(self._size):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


class MaxHeap(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count-1)  # 维持堆的特性

    def _siftup(self, ndx):
        if ndx > 0:
            parent = int((ndx-1)/2)
            if self._elements[ndx] > self._elements[parent]:    # 如果插入的值大于 parent，一直交换
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
                self._siftup(parent)    # 递归

    def extract(self):
        if self._count <= 0:
            raise Exception('empty')
        value = self._elements[0]    # 保存 root 值
        self._count -= 1
        self._elements[0] = self._elements[self._count]    # 最右下的节点放到root后siftDown
        self._siftdown(0)    # 维持堆特性
        return value

    def _siftdown(self, ndx):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        # determine which node contains the larger value
        largest = ndx
        if (left < self._count and     # 有左孩子
                self._elements[left] >= self._elements[largest] and
                self._elements[left] >= self._elements[right]):  # 原书这个地方没写实际上找的未必是largest
            largest = left
        elif right < self._count and self._elements[right] >= self._elements[largest]:
            largest = right
        if largest != ndx:
            self._elements[ndx], self._elements[largest] = self._elements[largest], self._elements[ndx]
            self._siftdown(largest)
            

class MinHeap(object):
    def __init__(self, maxsize = None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception("The heap is full!")
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count-1)

    def _siftup(self, index):
        if index > 0:
            parent = int((index - 1) / 2)
            if self._elements[parent] > self._elements[index]:
                self._elements[parent], self._elements[index] = self._elements[index], self._elements[parent]
                self._siftup(parent)

    def extract(self):
        if self._count <= 0:
            raise Exception('The heap is empty!')
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._siftdown(0)
        return value

    def _siftdown(self, index):
        if index < self._count:
            left = 2 * index + 1
            right = 2 * index + 2
            if left < self._count and right < self._count \
                and self._elements[left] <= self._elements[right] \
                and self._elements[left] <= self._elements[index]:
                self._elements[left], self._elements[index] = self._elements[index], self._elements[left]
                self._siftdown(left)
            elif left < self._count and right < self._count \
                and self._elements[left] >= self._elements[right] \
                and self._elements[right] <= self._elements[index]:
                self._elements[right], self._elements[index] = self._elements[index], self._elements[right]
                self._siftdown(left)

            if left < self._count and right > self._count \
                and self._elements[left] <= self._elements[index]:
                self._elements[left], self._elements[index] = self._elements[index], self._elements[left]
                self._siftdown(left)


if __name__ == '__main__':
    import random
    n = 5
    h = MinHeap(n)
    a = [3,2,5,1,4]
    for i in a:
        h.add(i)
    for i in range(n):
        print(h.extract())