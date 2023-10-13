'''
Time complexity: O(n)
Space complexity: O(1), since we only created a fast and slow pointer
Thought process:
- The brute force, naive approach would be to iterate through the LinkedList twice, to get the number of element, and to move to the middle of the list.
- However, we can optimize this using fast and slow pointers. If we set both slow and fast to the beginning of the list, and move fast twice while move slow once, then slow will reach the middle of the list while fast move to the end of the list.
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Initialize slow and fast, pointing to the head
        slow = fast = head
        # The condition of this loop is interesting to break down:
        #   - First, it helps us check the edge case, when head is None
        #   - Second, it can check if there exist two nodes (nullptr does count) after our  fast 
        while fast and fast.next:
            # Move slow once and fast twice
            slow = slow.next
            fast = fast.next.next
        # return slow, as it is currently in the middle of the LinkedList
        return slow