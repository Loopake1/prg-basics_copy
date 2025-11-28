import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
nums = queue.LifoQueue()
lst = [2,3,7,4,1,9,8]
# adds elements to the top of the stack
for num in lst:
    nums.put(num)
 
print(nums.get()+nums.get())
stack_sum = 0
print(nums.value,'here')
while not nums.empty():
    stack_sum+= nums.get()

## prints number of elements of the stack
print('Number of stack elements:', nums.qsize())
print(stack_sum,'sum of all stack elements except last 2')
"""
Note the order of the printed elements.
The last added element is printed first.
"""
