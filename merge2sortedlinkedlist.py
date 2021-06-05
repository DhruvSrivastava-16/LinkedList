class listnode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

List1_n1 = listnode(2)
List1_n2 = listnode(5)
List1_n3 = listnode(7)
List1_n1.next = List1_n2
List1_n2.next = List1_n3

List2_n1 = listnode(3)
List2_n2 = listnode(11)
List2_n1.next = List2_n2

temp1 = List1_n1
temp2 = List2_n1
Ans_hd = Ans_tail = listnode()

print("temp1: ",temp1, temp1.val )
print("temp2: ",temp2, temp2.val )
print("List2: ",List2_n1, List2_n1.val )


print("running....")


while temp1 and temp2:
    if temp1.val < temp2.val:
       # print("temp1.val < temp2.val",temp1.val,temp2.val)
        Ans_tail.next = temp1
        temp1 = temp1.next
    
    else:
        #print("temp1.val > temp2.val",temp1.val,temp2.val)
        Ans_tail.next = temp2
        temp2 = temp2.next

    Ans_tail = Ans_tail.next

Ans_tail.next = temp1 or temp2
Ans_hd = Ans_hd.next

while Ans_hd:
    print("List Item: ",Ans_hd.val)
    Ans_hd = Ans_hd.next;

