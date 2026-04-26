"""
# Merge Two Sorted Lists

- **ID:** 21
- **Difficulty:** EASY
- **Topic Tags:** Linked List, Recursion
- **Link:** [LeetCode Problem](https://leetcode.com/problems/merge-two-sorted-lists/description/)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def printList(self, list: Optional[ListNode]):
    #     while list:
    #         print(list.val, end=", ")
    #         list = list.next
    #     print()

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        # self.printList(list1)
        # self.printList(list2)
        head = ListNode()
        p = head
        while list1 and list2:
            # self.printList(head)
            if list1.val <= list2.val:
                p.next = list1
                list1 = list1.next
                p = p.next
                p.next = None
            else:
                p.next = list2
                list2 = list2.next
                p = p.next
                p.next = None
        if list1:
            p.next = list1
        elif list2:
            p.next = list2
        return head.next



