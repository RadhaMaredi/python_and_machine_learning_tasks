# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self,l1,l2):
        self.l1 = l1
        self.l2 = l2

    def addTwoNumbers(self,l1, l2):
        
        added = ListNode(val = (l1.val +l2.val) % 10) #to grab onces place
        carry_over = (l1.val +l2.val) // 10 #to get carry 0<10,1for >10
        current_node = added
        
        while (l1.next and l2.next):
            l1 = l1.next
            l2 = l2.next
            
            current_node.next = ListNode ( val = (carry_over + l1.val +l2.val) % 10)
            carry_over = (carry_over + l1.val +l2.val) // 10 #to get carry 0<10,1for >10
            current_node = current_node.next
            
        while(l1.next):
            l1 = l1.next
            current_node.next = ListNode ( val = (carry_over + l1.val) % 10)
            carry_over = (carry_over + l1.val) // 10 #to get carry 0<10,1for >10
            current_node = current_node.next
        
        while(l2.next):
            l2 = l2.next
            current_node.next = ListNode ( val = (carry_over + l2.val) % 10)
            carry_over = (carry_over + l2.val) // 10 #to get carry 0<10,1for >10
            current_node = current_node.next
        
        if (carry_over) > 0:
            current_node.next = ListNode(val = 1)
        
        return added

a = ListNode()

list_1 = list(map(int, input().split(",")))
list_2 = list(map(int, input().split(",")))

result = Solution.addTwoNumbers(list_1, list_2)

print(result)