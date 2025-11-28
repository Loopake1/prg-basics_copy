import queue
stk = queue.LifoQueue()

for char in input('Enter string: '):stk.put(char)
string_to_reverse= ''.join([stk.get() for x in range(stk.qsize())])
print(string_to_reverse)