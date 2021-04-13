"""Example of doubly linked list class and various methods for manipulating it's values.
"""


class Node:
    """Single node of a linked list with pointers
    to the next and previous values.
    """
    def __init__(self, value=None):
        self.value = value
        self.next_value = None
        self.prev_value = None


class DLinkedList:
    """Linked list class for nodes with pointers
    to the next and previous values.
    """
    def __init__(self):
        self.head_value = None

    def insert_at_beginning(self, data):
        """Inserts a new value at the beginning of the list."""
        # Create a new node
        new_node = Node(data)
        # Create pointers between new node and current head if it exists
        if self.head_value is not None:
            new_node.next_value = self.head_value
            self.head_value.prev_value = new_node
        # Reassign a head node
        self.head_value = new_node

    def insert_after(self, node, data):
        """Inserts a new value after the 'node' in between of existing nodes
        of the linked list.
        """
        # Check if the node is valid
        if node is None:
            return
        # Create a new node
        new_node = Node(data)
        # Reassign pointers between 3 nodes
        new_node.prev_value = node
        new_node.next_value = node.next_value
        node.next_value = new_node
        # Reassign pointer of the node following new node if it exists
        if new_node.next_value is not None:
            new_node.next_value.prev_value = new_node

    def insert_at_end(self, data):
        """Inserts a new value at the end of the linked list.
        """
        # Create a new node
        new_node = Node(data)
        # If the list was empty, assign a new node as it's head
        if self.head_value is None:
            self.head_value = new_node
            return
        # Else search for the last node in the list
        last_node = self.head_value
        while last_node.next_value is not None:
            last_node = last_node.next_value
        # Create pointers between new node and last node of the list
        last_node.next_value = new_node
        new_node.prev_value = last_node
        return

    def remove(self, data):
        """Removes a value from the list. If the list contains several
        equal values, removes the 1st one."""
        value = self.head_value
        # If the list is empty
        if value is None:
            print(f'Could not remove {data} from an empty list.')
            return
        # If we are removing a head value
        if value.value == data:
            self.head_value = self.head_value.next_value
            self.head_value.prev_value = None
            return
        # Else search for the value to remove
        while value is not None:
            if value.value == data:
                break
            value = value.next_value
        # If we did not find the value in the list
        if value is None:
            print(f'Could not find {data} in the list.')
            return
        # If we found a value, reassign pointers of it's predecessor and the value following it.
        prev_value = value.prev_value
        next_value = value.next_value
        prev_value.next_value = next_value
        if next_value is not None:
            next_value.prev_value = prev_value

    def print_values(self):
        """Prints values of the list."""
        value = self.head_value
        while value is not None:
            print(value.value)
            value = value.next_value

    def reverse(self):
        """Reverses the order of elements in the list."""
        # If the list is empty
        if self.head_value is None:
            return self.head_value
        # Temporary list to index the nodes
        temp_list = []
        value = self.head_value
        while value is not None:
            temp_list.append(value)
            value = value.next_value
        # Reassign pointers for each node starting from the 2nd
        # from the beginning and up to the 2nd from the end
        for ind in range(1, len(temp_list) - 1):
            temp_list[ind].prev_value = temp_list[ind + 1]
            temp_list[ind].next_value = temp_list[ind - 1]
        # Reverse pointers for the 1st and last nodes
        temp_list[0].prev_value = temp_list[1]
        temp_list[0].next_value = None
        temp_list[-1].next_value = temp_list[-2]
        temp_list[-1].prev_value = None
        # Change head value of the list
        self.head_value = temp_list[-1]


# Initialize a doubly linked list
dl_list = DLinkedList()

# Add values
dl_list.insert_at_beginning(1)
dl_list.insert_at_beginning(2)
dl_list.insert_at_beginning(3)
dl_list.insert_at_beginning(4)
dl_list.insert_at_beginning(5)
dl_list.insert_after(dl_list.head_value.next_value, 8)
dl_list.insert_at_end(10)

# Check the result
dl_list.print_values()

# Reverse the list
dl_list.reverse()
print('Reversed list:')
dl_list.print_values()

# Remove value
dl_list.remove(3)
print('After removing:')
dl_list.print_values()
