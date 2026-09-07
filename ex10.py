class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, job, priority):
        self.heap.append((priority, job))
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index][0] > self.heap[parent][0]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def extract_max(self):
        if len(self.heap) == 0:
            print("Heap is empty!")
            return None

        max_job = self.heap[0]
        last = self.heap.pop()

        if len(self.heap) > 0:
            self.heap[0] = last
            self.heapify_down(0)

        return max_job

    def heapify_down(self, index):
        n = len(self.heap)

        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left][0] > self.heap[largest][0]:
                largest = left

            if right < n and self.heap[right][0] > self.heap[largest][0]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

    def peek(self):
        if len(self.heap) == 0:
            print("Heap is empty!")
        else:
            priority, job = self.heap[0]
            print("Highest Priority Job:", job)
            print("Priority:", priority)

    def display(self):
        if len(self.heap) == 0:
            print("Heap is empty!")
        else:
            print("Jobs in Heap Order:")
            for priority, job in self.heap:
                print("Job:", job, "| Priority:", priority)


heap = MaxHeap()

while True:
    print("\n1. Insert Job")
    print("2. Delete Highest Priority Job")
    print("3. Peek Highest Priority Job")
    print("4. Display All Jobs")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        job = input("Enter Job Name: ")
        priority = int(input("Enter Job Priority: "))
        heap.insert(job, priority)
        print("Job inserted successfully!")

    elif choice == 2:
        result = heap.extract_max()

        if result is not None:
            priority, job = result
            print("Processed Job:", job)
            print("Priority:", priority)

    elif choice == 3:
        heap.peek()

    elif choice == 4:
        heap.display()

    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice!")
