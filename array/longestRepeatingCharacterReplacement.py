'''
Time complexity: O(n)
Space complexity: O(n)
Thought process:
- Use sliding windows method to determine the most frequent character in a substring. Take the substring's length, minus the # of occurences of the most frequent character,
  we have the number of characters that can be replaced. That number must be < the given k, in order for a replacement to be valid.
- To keep up with the count/frequency of each character in the string, use a dictionary. For each time the right pointer move forward, we add a character. 
  However, for each time the left pointer move forward, we remove the previous character at the left pointer.
'''

from typing import List
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        left, right = 0, 0
        while right < len(s):
            if s[right] not in count:
                count[s[right]] = 1
            else:
                count[s[right]] += 1
            # Calculate k value of the window = size of window - # of most frequent element
            temp = (right - left + 1) - max(count.values())
            if temp > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, (right - left + 1))
            right += 1
        return result