"""Example of singly linked list class and various methods for manipulating it's values.
"""


class Node:
    """Single node of a linked list with pointer to the next value.
    """
    def __init__(self, value=None):
        """Node could be initialized with or without a value.
        """
        self.value = value
        self.next_value = None


class SLinkedList:
    """Linked list class for nodes with pointers to the next value.
    """
    def __init__(self):
        self.head_value = None

    def print_values(self):
        """Prints all values of the linked list in their order."""
        value = self.head_value
        while value is not None:
            print(value.value)
            value = value.next_value

    def insert_at_beginning(self, data):
        """Inserts a new value at the beginning of the lined list.
        """
        # Add a new node pointing to the current head node
        new_node = Node(data)
        new_node.next_value = self.head_value
        self.head_value = new_node

    def insert_at_end(self, data):
        """Inserts a new value at the end of the linked list.
        """
        new_node = Node(data)
        # If the list is empty, assign new node as a single value
        if self.head_value is None:
            self.head_value = new_node
            return
        # If list contains values, search for the last node
        last_node = self.head_value
        while last_node.next_value:
            last_node = last_node.next_value
        # Add a pointer from the last value to a new node
        last_node.next_value = new_node

    def insert_after(self, node, data):
        """Inserts a new value after the 'node' in between of existing nodes
        of the linked list.
        """
        # Check that the middle node is valid
        if node is None:
            print(f'{node} is not in the tree.')
            return
        try:
            # Reassign a pointer from 'middle_node' to new node,
            # and from new node to the next value following 'middle_node'.
            new_node = Node(data)
            new_node.next_value = node.next_value
            node.next_value = new_node
        except Exception as e:
            print('Error in executing insert_after():', e)
            print(f'{data} could not be inserted after node {node}.')
            print(f'Check that {node} is a valid node of the list or try insert_at_end().')

    def remove(self, data):
        """Removes a node from the linked list.
        """
        head_value = self.head_value

        # If the list is empty
        if head_value is None:
            print(f'Could not remove {data} from an empty list.')
            return

        # If we are removing a head value
        if head_value.value == data:
            self.head_value = self.head_value.next_value
            return

        # Else search for the value to remove
        while head_value is not None:
            if head_value.value == data:
                break
            prev_value = head_value
            head_value = head_value.next_value

        # If we did not find the value in the list
        if head_value is None:
            print(f'Could not find {data} in the list.')
            return
        # If we found a value, reassign a pointer from it's predecessor to the next value.
        prev_value.next_value = head_value.next_value

    def cycles(self):
        """Searches for cycles in the list and returns a tuple
        where the fist element is a binary value (True or False),
        and the second element is the node value pointing to one of it's predecessors,
        the third element is numerical index of the node in a list where the cycle starts.
        If the list contains multiple cycles, returns only the first instance.
        If no cycles were detected, returns (False, None, -1).
        """
        # Variables to be returned if there is no cycle
        flag = False
        node = None

        cur_value = self.head_value
        seen_values = dict()
        index = 0

        while cur_value:
            # If we pass a node for the second time
            if cur_value in seen_values:
                flag = True
                node = prev_value.value
                break
            seen_values[cur_value] = index
            prev_value = cur_value
            cur_value = cur_value.next_value
            index += 1

        if not flag:
            index = -1
        else:
            index = seen_values[cur_value]

        return flag, node, index

    def reorder(self):
        """Reorders the nodes in a linked list from L0 → L1 → ... → Ln - 1 → Ln
        to L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → ... by changing nodes themselves,
        without changing node values.
        """
        # Create a temporary list to index nodes in their current order
        temp_list = []
        cur_value = self.head_value
        while cur_value:
            temp_list.append(cur_value)
            cur_value = cur_value.next_value

        n_nodes = len(temp_list)
        # Only if the list contains more than 2 nodes and we have to reorder
        if n_nodes > 2:
            # Go through the first half of indexes and create a reordered index list
            reordered_index = []
            half_index = n_nodes // 2
            for index in range(half_index):
                reordered_index.append(index)
                reordered_index.append(n_nodes - 1 - index)
            # If the list has odd number of elements, add the index of middle element
            if n_nodes % 2 == 1:
                reordered_index.append(half_index)
            # Reassign pointers for all elements except the last one,
            # according to the new order
            for i in range(n_nodes - 1):
                temp_list[reordered_index[i]].next_value = temp_list[reordered_index[i+1]]
            # Delete pointer of the last element
            temp_list[reordered_index[-1]].next_value = None


# Initialize a linked list and assign a head value
l_list = SLinkedList()
l_list.head_value = Node('Mon')

# Create a couple of new nodes and connect them to the head
node_1 = Node('Tue')
node_2 = Node('Wed')
l_list.head_value.next_value = node_1
node_1.next_value = node_2

# Insert values at different places
l_list.insert_at_beginning('Sat')
l_list.insert_at_end('Thu')
l_list.insert_at_end('Fr')
l_list.insert_after(l_list.head_value, 'Sun')

print('Before reordering:')
l_list.print_values()
print('After reordering:')
l_list.reorder()
l_list.print_values()

# Remove a value
l_list.remove('Thu')

# Check the list values
print('After removing:')
l_list.print_values()

# Create a cycle and detect it
node_2.next_value = l_list.head_value
print('Search for cycles:')
print(l_list.cycles())
