# x = [4, 6, 2, 1, 7, 9]
# x = ['想', '额r']
# x.sort(key=len, reverse=True)  # 数字、字符串按照ASCII，中文按照unicode从小到大排序；不会混合比较
# print(x)  # [1, 2, 4, 6, 7, 9]
# # sorted返回一个有序的副本，并且类型总是列表
# print(sorted('Python',key=len))  # ['P', 'h', 'n', 'o', 't', 'y']


# class ZHeap:  # 小根堆
#     def __init__(self, item=[]):
#         # 初始化。item为数组
#         self.items = item
#         self.heapsize = len(self.items)
#
#     def LEFT(self, i):
#         return 2 * i + 1
#
#     def RIGHT(self, i):
#         return 2 * i + 2
#
#     def PARENT(self, i):
#         return (i - 1) // 2
#
#     def MIN_HEAPIFY(self, i):
#         # 最小堆化：使以i为根的子树成为最小堆
#         l = self.LEFT(i)
#         r = self.RIGHT(i)
#         if l < self.heapsize and self.items[l] < self.items[i]:
#             smallest = l
#         else:
#             smallest = i
#
#         if r < self.heapsize and self.items[r] < self.items[smallest]:
#             smallest = r
#
#         if smallest != i:
#             self.items[i], self.items[smallest] = self.items[smallest], self.items[i]
#             self.MIN_HEAPIFY(smallest)
#
#     def INSERT(self, val):
#         # 插入一个值val，并且调整使满足堆结构
#         self.items.append(val)
#         idx = len(self.items) - 1
#         parIdx = self.PARENT(idx)
#         while parIdx >= 0:
#             if self.items[parIdx] > self.items[idx]:
#                 self.items[parIdx], self.items[idx] = self.items[idx], self.items[parIdx]
#                 idx = parIdx
#                 parIdx = self.PARENT(parIdx)
#             else:
#                 break
#         self.heapsize += 1
#
#     def DELETE(self):
#         last = len(self.items) - 1
#         if last < 0:
#             # 堆为空
#             return None
#         # else:
#         self.items[0], self.items[last] = self.items[last], self.items[0]
#         val = self.items.pop()
#         self.heapsize -= 1
#         self.MIN_HEAPIFY(0)
#         return val
#
#     def BUILD_MIN_HEAP(self):
#         # 建立最小堆, O(nlog(n))
#         i = self.PARENT(len(self.items) - 1)
#         while i >= 0:
#             self.MIN_HEAPIFY(i)
#             i -= 1
#
#     def SHOW(self):
#         print(self.items)
#
#
# class ZPriorityQ(ZHeap):
#     def __init__(self, item=[]):
#         ZHeap.__init__(self, item)
#
#     def enQ(self, val):
#         ZHeap.INSERT(self, val)
#
#     def deQ(self):
#         val = ZHeap.DELETE(self)
#         return val
#
#
# a = [1, 3, 2, 4, 8, 6, 22, 9]
# pq = ZPriorityQ(a)
# n = len(a)
# # for i in range(n):
# #     pq.enQ(a[i])
# #     pq.SHOW()
#
# for i in range(n):
#     pq.deQ()
#     pq.SHOW()

# class BinaryHeap:  # 大根堆
#     def __init__(self, n):
#         self.heap = [0] * n
#         self.size = 0
#
#     def remove_min(self):
#         removed = self.heap[0]
#         self.size -= 1
#         self.heap[0] = self.heap[self.size]
#         self._down(0)
#         return removed
#
#     def add(self, value):
#         self.heap[self.size] = value
#         self._up(self.size)
#         self.size += 1
#
#     def _up(self, pos):
#         while pos > 0:
#             parent = (pos - 1) // 2
#             if self.heap[pos] >= self.heap[parent]:
#                 break
#             self.heap[pos], self.heap[parent] = self.heap[parent], self.heap[pos]
#             pos = parent
#
#     def _down(self, pos):
#         while True:
#             child = 2 * pos + 1
#             if child >= self.size:
#                 break
#             if child + 1 < self.size and self.heap[child + 1] < self.heap[child]:
#                 child += 1
#             if self.heap[pos] <= self.heap[child]:
#                 break
#             self.heap[pos], self.heap[child] = self.heap[child], self.heap[pos]
#             pos = child
#
#
# h = BinaryHeap(10)
# h.add(5)
# h.add(7)
# h.add(9)
# h.add(4)
# h.add(3)
# h.add(3)
# h.add(3)
# h.add(3)
# print(h.heap)
# h.add(1)
# print(h.heap)
# h.add(2)
# print(h.heap)
# print(h.remove_min())
# print(h.remove_min())
# print(h.remove_min())
