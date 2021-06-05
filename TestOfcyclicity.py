#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 21:24:11 2021

@author: dhruv
"""

class listnode:
    def __init__(self,val=0,next=None):
        self.data = val
        self.next = next
        
List1_n1 = listnode(11)
List1_n2 = listnode(3)
List1_n3 = listnode(5)
List1_n4 = listnode(7)
List1_n5 = listnode(2)
List1_n6 = listnode(1)

List1_n1.next = List1_n2
List1_n2.next = List1_n3
List1_n3.next = List1_n4
List1_n4.next = List1_n5
List1_n5.next = List1_n3

def testofcyclicity(head):
    slow = head;
    fast = head;
    
    while (slow and fast.next):
        print("Yo")
        
        slow = slow.next
        fast = fast.next.next
    
        if slow == fast:
            print("Cycle Exists!")
            return 
        
    print("Cycle Not Exists!!")
    
testofcyclicity(List1_n1)

        
    