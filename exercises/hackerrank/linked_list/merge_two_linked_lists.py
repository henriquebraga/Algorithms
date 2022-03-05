#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    
    if head1 is None and head2 is None:
        return None
    
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    if head1.data > head2.data:
        node = head2
        head2 = head1
        head1 = node
    
    list_head = head1

    while head2 is not None:
        while head1.next is not None and head2.data > head1.next.data:
            head1 = head1.next
            
        _next_2 = head2.next
        head2.next = head1.next
        head1.next = head2
        head2 = _next_2
    return list_head
            
            #4 5 6
            #1 2 3

            
# Node* MergeLists(Node *headA, Node* headB)
# {
#     if (headA == NULL && headB == NULL) {
#         return NULL;
#     }

#     if (headA == NULL) {
#         return headB;
#     }

#     if (headB == NULL) {
#         return headA;
#     }

#     // Ensure that list A starts with the smaller number
#     if (headA->data > headB->data) {
#         Node *tmp = headB;
#         headB = headA;
#         headA = tmp;
#     }

#     Node *listHead = headA;

#     while (headB) {
#         // Advance through nodes in list A until the next node
#         // has data bigger than data at current node of list B
#         while (headA->next != NULL &&
#                headB->data > headA->next->data) {
#             headA = headA->next;
#         }

#         // Insert current node in list B into list A
#         Node* nextB = headB->next;
#         headB->next = headA->next;
#         headA->next = headB;
#         headB = nextB;
#     }

#     return listHead;
# }
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
