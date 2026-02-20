
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums)

print("nums.pop()")
nums.pop()
print(nums)

print("nums.append(20)")
nums.append(20)
print(nums)

print("nums.insert(3, 99)")
nums.insert(3, 99)
print(nums)

print("del nums[1]")
del nums[1]
print(nums)

# double end queue
from collections import deque
lst = deque([1,2,3,4,5])
print("\n---deque test---")
print("lst.appendleft(0)")
lst.appendleft(0)
print(lst)

print("lst.append(6)")
lst.append(6)
print(lst)

print("lst.popleft()")
lst.popleft()
print(lst)

print("lst.pop()")
lst.pop()
print(lst)

print("del lst[1]")
del lst[1]
print(lst)

print("lst.insert(2,99)")
lst.insert(2,99)
print(lst)
