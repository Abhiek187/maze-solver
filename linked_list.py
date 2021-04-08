class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        # Print the entire linked list
        curr = self.head
        output = ""

        while curr is not None:
            output += str(curr.value)

            if curr.next is not None:
                output += " -> "  # connect an arrow to the next node

            curr = curr.next

        return output

    def insert(self, value):
        # Insert the value into the linked list and return true if a new node was created
        curr = self.head

        if curr is None:
            # Set the first node as the head of the linked list
            self.head = Node(value)
            return True

        while True:
            # The value already exists in the linked list
            if curr.value == value:
                return False

            if curr.next is None:
                # Create a new node
                curr.next = Node(value)
                return True
            else:
                curr = curr.next

    def get_value(self, value):
        # Search for the value in the linked list
        curr = self.head

        while curr is not None:
            if curr.value == value:
                return curr.value

            curr = curr.next

        return -1  # default value if the element doesn't exist

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
