import queue

def dec_to_b(n):
    bin_stack = queue.LifoQueue()

    while n>0:
        
        bin_stack.put(n%2)
        n //=2
    return bin_stack
b_stack = dec_to_b(18)
while b_stack.empty() == False:
    print(b_stack.get(),end='')
    3