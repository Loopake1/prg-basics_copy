import queue
from operator import *

stk = queue.LifoQueue()
str_ops = {'-': sub,'+':add,'*':mul,'/':truediv}
expression = input('Enter expression')
result = 0
for expr in expression:
    if expr in [str(x) for x in range(10)]:
        stk.put(expr)
    elif expr in str_ops.keys():
        num2 = int(stk.get())
        num1 = int(stk.get())
        stk.put(str_ops[expr](num1,num2))
    elif expr == '=':
        print(stk.get(),'result')
        break
    else:
        continue
