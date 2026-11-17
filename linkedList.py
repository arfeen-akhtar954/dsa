# Question 1: Traversal
# class Node():
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# def deleteHead(head):
#     if head is None:
#         return None
#     head=head.next
#     return head
    
# def traversal(head):
#     arr=[]
#     temp=head
#     while temp is not None:
#         arr.append(temp.data)
#         temp=temp.next
#     return arr
# head=Node(1)
# second=Node(2)
# third=Node(3)

# head.next=second
# second.next=third

# head=deleteHead(head)
# print(traversal(head))