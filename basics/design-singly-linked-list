# Design Singly Linked List
# Test Cases Cleared: 15/15
# Neetcode link: https://neetcode.io/problems/singlyLinkedList

class Node:
    def __init__(self, val: int):
        self.value = val
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    
    def get(self, index: int) -> int:
        """Get node at a given index. Return node if it exists else Return -1."""
        if index <0 or index >= self.length:
            return -1
        else:
            current_node = self.head
            for index in range(index):
                current_node = current_node.next
            return  current_node.value


    def insertHead(self, val: int) -> None:
        """Insert head node."""
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1


    def insertTail(self, val: int) -> None:
        """Insert tail node."""
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


    def removeHead(self):
        """Remove head node."""
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            next_node = self.head.next
            self.head.value = next_node.value
            self.head.next = next_node.next
        self.length -= 1


    def removeTail(self):
        """Remove tail node"""
        current_node = self.head
        for index in range(self.length - 2):
            current_node = current_node.next  
        self.tail = current_node
        self.tail.next = None
        self.length -= 1


    def remove(self, index: int) -> bool:
        """Remove node at a given index. Return True if node exists else Return False."""
        if index <0 or index >= self.length:
            return False
        elif index == 0:
            self.removeHead()
            return True
        elif index == self.length - 1:
            self.removeTail()
            return True
        else:
            current_node = self.head
            for index in range(index - 1):
                current_node = current_node.next
            current_node.next = current_node.next.next
            self.length -= 1
            return True
        

    def getValues(self) -> List[int]:
        """Get all node values as a list."""
        if self.length == 0:
            return []
        else:
            my_list = []
            current_node = self.head
            while current_node.next is not None:
                my_list.append(current_node.value)
                current_node = current_node.next
            my_list.append(current_node.value)
            return my_list
        
