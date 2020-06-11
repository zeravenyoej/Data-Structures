class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node 
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_to_tail(self, value):
        new_node = Node(value, None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    def remove_head(self):
        if not self.head:
            return None
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value
    def remove_tail(self):
        if not self.head:
            return None
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        current = self.head
        while current.get_next() is not self.tail:
            current = current.get_next()
        value = self.tail.get_value()
        self.tail = current
        return value
    def contains(self, value):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False
    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.get_value()
        current = self.head.get_next()
        while current:
            if current.get_value() > max_value:
                max_value = current.get_value()
            current = current.get_next()
        return max_value

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    def __len__(self):
        return self.size
  #    * `push` adds an item to the top of the stack.
    def push(self, value):
        # make the tail point to the new_node. it'll be the last one in, therefore the first one out
        self.size +=1
        self.storage.add_to_tail(value)
  #    * `pop` removes and returns the element at the top of the stack
    def pop(self):
        # last in should be the first out
        if self.size == 0:
            return None
        self.size -=1
        return self.storage.remove_tail()

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    def __len__(self):
        return self.size
  #    * `enqueue` adds an element to the back of the queue.
    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)
  #    * `dequeue` removes and returns the element at the front of the queue.
    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_head()

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
    on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # Insert the given value into the tree
    def insert(self, value):
        # comparing against the value of the root
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else: 
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else: 
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            else: 
                return self.right.contains(target)
    # Return the maximum value found in the tree
    def get_max(self):
        max = self.value         
        if self.right is None:
            return max
        else: 
            max = self.right.value
            return self.right.get_max()
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 ---------------------------------------------------------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return 
        self.in_order_print(node.left)        # keep running down the left side until there isn't one
        print(node.value)                     # as soon as there isn't anything to the left. print the value
        self.in_order_print(node.right)       # now run down the right side until there isn't one. 


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        tree = Queue()                      # use a queue
        tree.enqueue(node)                  # start queue with root node
        while tree.__len__() > 0:           # while loop that checks size of queue
            current = tree.dequeue()        # returns the element at the front of the queue and makes assigns it to 'current'
            if current.left:                # check to see if there's a valid node on the left
                tree.enqueue(current.left)  # add the left node to the queue 
            if current.right:               # check to see if there's a vlid node on the right
                tree.enqueue(current.right) # add the right node to the queue
            print(current.value)            # print the current node


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        tree = Stack()
        tree.push(node)
        while tree.__len__() > 0:
            current = tree.pop()
            if current.left:
                tree.push(current.left)
            if current.right:
                tree.push(current.right)
            print(current.value)


    # # Stretch Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
