class LinkedList:
    class Node:
        def __init__(self, value, weight, heuristic):
            self.value = value
            self.weight = weight
            self.end_weight = heuristic
            self.next = None

    def __init__(self):
        self.head = None

    def insert(self, value, weight=0, heuristic=0):
        # Insert the value into the linked list and return true if a new node was created
        curr = self.head

        if curr is None:
            # Set the first node as the head of the linked list
            self.head = self.Node(value, weight, heuristic)
            return True

        while True:
            # The value already exists in the linked list
            if curr.value == value:
                return False

            if curr.next is None:
                # Create a new node
                curr.next = self.Node(value, weight, heuristic)
                return True
            else:
                curr = curr.next

    def remove_head(self):
        # Replace the head with its next element
        head = self.head

        if head is not None:
            self.head = self.head.next

        return head

    def remove(self, value):
        # Remove the value from the linked list
        prev = None
        curr = self.head

        while curr is not None:
            if curr.value == value:
                if prev is None:
                    # Set the head as the next node
                    self.head = curr.next
                else:
                    # Link the previous node to the next node
                    prev.next = curr.next

                return curr

            prev = curr
            curr = curr.next

        return None
