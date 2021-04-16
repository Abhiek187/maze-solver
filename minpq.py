class MinPQ:
    def __init__(self, max_e):
        # A priority queue of the vertex and weight (sorted by weights)
        self.pq = [[-1 for _ in range(2)] for _ in range(max_e)]  # pq[0] is unused
        self.size = 0

    def __swap(self, i1, i2):
        # Swap indices i1 and i2 in the priority queue
        temp = self.pq[i1]
        self.pq[i1] = self.pq[i2]
        self.pq[i2] = temp

    def __swim(self, i):
        # Move an element up to its proper index
        k = i

        # Stop once the top is reached or the parent is smaller than the child
        while k > 1 and self.pq[k // 2][1] > self.pq[k][1]:
            # Swap the parent and the child
            self.__swap(k, k // 2)
            k //= 2  # keep k as an int

    def insert(self, value):
        # Insert the element at the end of the min-heap and swim it up
        self.size += 1
        self.pq[self.size] = value
        self.__swim(self.size)

    def __sink(self, i):
        # Move an element down to its proper index
        k = i

        # Stop once the bottom is reached or both children are greater than the parent
        while 2 * k <= self.size:
            j = 2 * k

            # Compare the smaller of the two children with the parent
            if j < self.size and self.pq[j][1] > self.pq[j + 1][1]:
                j += 1
            if self.pq[k][1] <= self.pq[j][1]:
                break

            self.__swap(k, j)
            k = j

    def del_min(self):
        # Delete the top element, swap with the last element, and then sink it down
        min_e = self.pq[1]
        self.__swap(1, self.size)
        self.size -= 1
        self.__sink(1)
        self.pq[self.size + 1] = []
        return min_e

    def is_empty(self):
        return self.size == 0

    def update_or_insert(self, value):
        # If the vertex already exists, update its weight, or add it to the queue
        for i in range(1, self.size + 1):
            if self.pq[i][0] == value[0]:
                self.pq[i][1] = value[1]
                return

        self.insert(value)
