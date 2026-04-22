"""
# Insert Delete GetRandom O(1)

- **ID:** 380
- **Difficulty:** MEDIUM
- **Topic Tags:** Array, Hash Table, Math, Design, Randomized
- **Link:** [LeetCode Problem](https://leetcode.com/problems/insert-delete-getrandom-o1/description/)

Implement the RandomizedSet class:
- RandomizedSet() Initializes the RandomizedSet object.
- bool insert(int val) Inserts an item val into the set if not present.
  Returns true if the item was not present, false otherwise.
- bool remove(int val) Removes an item val from the set if present.
  Returns true if the item was present, false otherwise.
- int getRandom() Returns a random element from the current set of elements.
  Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works
in average O(1) time complexity.

Constraints:
-2^31 <= val <= 2^31 - 1
At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
There will be at least one element when getRandom is called.

Example 1:
Input:  ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
        [[],[1],[2],[2],[],[1],[2],[]]
Output: [null, true, false, true, 2, true, false, 2]
"""
import random

class RandomizedSet:
    def __init__(self):
        self.container_list = []
        self.container_dic = {}

    def insert(self, val: int) -> bool:
        if val not in self.container_dic:
            self.container_list.append(val)
            self.container_dic[val] = len(self.container_list) - 1
            return True
        else:
            return False
    
    def remove(self, val: int) -> bool:
        if val in self.container_dic:
            idx = self.container_dic[val]
            last = self.container_list[-1]
            self.container_list[idx] = last
            self.container_dic[last] = idx
            self.container_list.pop()
            del self.container_dic[val]
            return True
        else:
            return False
    
    def getRandom(self) -> int:
        if len(self.container_list) == 0:
            return -1
        return random.choice(self.container_list)
    
    def print(self):
        print(self.container_dic)
        print(self.container_list)

rs = RandomizedSet()
for i in range(1,6):
    rs.insert(i)
rs.print()

rs.remove(5)
rs.print()

print(rs.getRandom())
