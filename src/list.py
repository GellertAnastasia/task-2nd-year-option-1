from src.node import Node


class List:

    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def append_multiple(self, values):
        for value in values:
            self.append(value)

    def is_symmetric(self):
        if not self.head or not self.head.next:
            return True

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        first_half = self.head
        second_half = prev

        while second_half:
            if first_half.value != second_half.value:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

    def print_list(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.value))
            current = current.next
        print(" ".join(result))
