class ListNode:
    def __init__(self,value=0,next=None):
        self.data = value
        self.next = next

def search(head,key):
    temp = head
    loc = 1
    while(temp):
        
        if temp.data == key:
            print("Found! and it is at Node: ",loc,"\n")
            return 
        
        temp = temp.next
        loc+=1
    
    print("Not Found!! \n")

def insertnew(head,value,after):
    #temp = head;
    #while temp.next:
        #temp = temp.next
    newnode = ListNode(99)
    if after.next:
        temp = after.next 
        after.next= newnode
        newnode.next = temp

    else:
        after.next = newnode
    
    return newnode

def delete(node): #delete the node which is next to this node
    #if node to be deleted is not tail
    node.next = node.next.next


head = ListNode(3)
node2 = ListNode(4)
node3 = ListNode(5)
node4 = ListNode(6)
node5 = ListNode(7)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

search(head,6)
search(head,99)
insertnew(head,99,node3)
search(head,99)

temp = head;

while temp:
    print("List Item: ",temp.data)
    temp = temp.next;

delete(node3)


temp = head;

print("\n \n --------")

while temp:
    print("List Item: ",temp.data)
    temp = temp.next;
