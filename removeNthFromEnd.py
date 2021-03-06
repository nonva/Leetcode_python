#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-03-13
@author: Ting Wang
'''

#Given a linked list, remove the nth node from the end of list and return its head.
#For example,
#   Given linked list: 1->2->3->4->5, and n = 2.
#   After removing the second node from the end, the linked list becomes 1->2->3->5.
#Note:
#Given n will always be valid.
#Try to do this in one pass.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head == None:
            return head
        if head.next == None:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        q = dummy
        for i in range(n):
            q = q.next
        while q.next != None:
            p = p.next
            q = q.next
        # delete p, the Nth node from the end
        tmp = p.next
        p.next = p.next.next
        del tmp
        return dummy.next