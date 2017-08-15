# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ans = ListNode(x = None)
        rtype = ans
        plus = 0
        while l1.next != None and l2.next != None: 
            if plus == 0:
                rtype.val = l1.val + l2.val
            else:
                rtype.val = l1.val + l2.val + 1
            if rtype.val >= 10:
                rtype.val = rtype.val - 10
                plus = 1
            else:
                plus = 0
            l1 = l1.next
            l2 = l2.next
            rtype.next = ListNode(x= None)
            rtype = rtype.next
        if l1.next != None and l2.next == None:
            temp = l2.val
            while l1.next != None:
                if plus == 0:
                    rtype.val = l1.val + temp
                else:
                    rtype.val = l1.val + temp + 1
                if rtype.val >= 10:
                    rtype.val = rtype.val - 10
                    plus = 1
                else:
                    plus = 0
                temp = 0
                l1 = l1.next
                rtype.next = ListNode(x= None)
                rtype = rtype.next
            if plus == 1:
                rtype.val = l1.val + 1
                if rtype.val >= 10:
                    rtype.val = rtype.val - 10
                    rtype.next = ListNode(x= 1)
            else:
                rtype.val = l1.val
            return ans
        elif l2.next != None and l1.next == None:
            temp = l1.val
            while l2.next != None:
                if plus == 0:
                    rtype.val = l2.val + temp
                else:
                    rtype.val = l2.val + temp + 1
                if rtype.val >= 10:
                    rtype.val = rtype.val - 10
                    plus = 1
                else:
                    plus = 0
                temp = 0
                l2 = l2.next
                rtype.next = ListNode(x= None)
                rtype = rtype.next
            if plus == 1:
                rtype.val = l2.val + 1
                if rtype.val >= 10:
                    rtype.val = rtype.val - 10
                    rtype.next = ListNode(x= 1)
            else:
                rtype.val = l2.val
            return ans
                
        if plus == 0:
            rtype.val = l1.val + l2.val
        else:
            rtype.val = l1.val + l2.val + 1
        if rtype.val >= 10:
            rtype.val = rtype.val - 10
            rtype.next = ListNode(x= 1)
        else:
            rtype.next = None
        return ans
                 
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
# 感受到大佬的压制......

def addTwoNumbers(self, l1, l2):
    dummy = cur = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        cur.next = ListNode(carry%10)
        cur = cur.next
        carry //= 10
    return dummy.next
