#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

# Got from @github.com/liyaSileshi, better than my idea
class llIterator:
    def __init__(self, head):
        self.curr = head

    def __iter__(self):
        return self

    def __next__(self):
        while self.curr != None:
            item = self.curr.data
            self.curr = self.curr.next
            return item
        raise StopIteration

class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) because we are looping so it depends on how many objects are in the linked list"""
        # length = 0
        # this_node = self.head
        # while this_node != None:
        #     this_node = this_node.next
        #     length += 1
        # return length
        return self.size

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1), only needs to find the tail and add itself after that and call the tail pointer to it."""
        node = Node(item)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self.size += 1
        

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) because no matter what, it only needs to run once to prepend a node."""
        node = Node(item)
        if not self.is_empty(): #If there are nodes
            node.next = self.head
        else:
            self.tail = node
        self.head = node
        self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best Case: O(1) because the first node could possess the quality
        Worst case running time: O(n) because it might have to run until the last node is checked and the quality returned/analyzed"""
        if not self.is_empty(): #If there are nodes
            current_node = self.head
            while current_node is not None: # While there's still nodes to become the current node
                if quality(current_node.data) is True: # Checks if the node's data possesses the quality
                    return current_node.data
                else:
                    current_node = current_node.next
        else:
            return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) because if our first item satisfies the given
        item, we are done.
        Worst case running time: O(n) because we are searching through all n
        nodes and we could check all of them."""
        previous_node = None
        current_node = self.head
        is_found = False
        if self.is_empty(): #If there are no nodes
            raise ValueError('Error: word not found: {}'.format(item))
        elif self.head == self.tail: #If there is only one node
            if current_node.data == item:
                self.head = None
                self.tail = None
                self.size -= 1
            else:
                raise ValueError('Error: word not found: {}'.format(item))
        else:
            while current_node is not None:
                if current_node.data == item:
                    is_found = True
                    if previous_node is None: #If node was the first one
                        self.head = current_node.next
                    elif current_node == self.tail: #If node was the last one
                        self.tail = previous_node
                        previous_node.next = None
                    else:
                        previous_node.next = current_node.next
                previous_node = current_node
                current_node = current_node.next
            self.size -= 1
            if is_found is False:
                raise ValueError('Error: item not found: {}'.format(item))

    def replace(self, item, new_data):
        """Replace a item in our linked-list with a new item"""
        # Best and worst case are both O(n).

        #set current node to the head of list
        current_node = self.head

        # Iterate through the linked list until the node data is equal to the item
        while current_node is not None:
            if current_node.data == item:
                current_node.data = new_data
                return None
            current_node = current_node.next
        # Raise error if no item is found  
        raise ValueError(f'Item not found: {item}')


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
