#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 19:02:35 2021

@author: dhruv
"""

class listnode:
    def __init__(self,val = 0,next = None):
        self.val = val;
        self.next = next
        


def reverse_sublist(List1_n1,s,f):
    print("Yo!")
    
    dummy_head = List1_n1
    sublist_head = listnode();
    temp = List1_n1
    
    
    for _ in range(1,s-1):
        temp = temp.next
        
    sublist_head = temp
    print(temp.val)   #we have reached the predecessor of the sublist head
    
    sublist_iter = temp.next #we are address 3
    
    for _ in range(f-s):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next 
        sublist_head.next = temp 
        
        




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
List1_n5.next = List1_n6

s = 2
f = 4
                                    
reverse_sublist(List1_n1,s,f)