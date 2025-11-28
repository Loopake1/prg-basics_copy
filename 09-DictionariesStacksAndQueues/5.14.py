import queue
q = queue.Queue()
while True:
    customer = input('Enter customer name, to end enter Quit or press Enter')
    if customer.lower() == 'quit' or customer == '':
        break
    
    print(f'There is {q.qsize()} customers before customer {customer}')
    q.put(customer)
