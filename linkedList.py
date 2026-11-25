# Question 1: Traversal
class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

def deleteHead(head):
    if head is None:
        return None
    head=head.next
    return head
    
def deleteTail(head):
    if head is None:
        return None
    if head.next is None:
        return None
    temp=head
    while temp.next.next is not None:
        temp=temp.next
    temp.next=None
    return head

def deleteKthElement(head, k):
    if head is None:
        return None
    if k==1:
        head=head.next
        return head
    temp=head
    for i in range(k-2):
        temp=temp.next
    temp.next=temp.next.next
    return head

def insertHead(head, value):
    newNode=Node(value)
    if head is None:
        head=newNode
        return head
    newNode.next=head
    head=newNode
    return head
    
def deleteValue(head, X):
    if head is None:
        return None
    if X==head.data:
        head=head.next
        return head
    temp=head
    while temp.next.data is not X:
        temp=temp.next
    temp.next=temp.next.next
    return head

def traversal(head):
    arr=[]
    temp=head
    while temp is not None:
        arr.append(temp.data)
        temp=temp.next
    return arr

head=Node(10)
second=Node(20)
third=Node(30)

head.next=second
second.next=third

head=insertHead(head,5)
print(traversal(head))