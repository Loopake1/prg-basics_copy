import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct
expr = '(2-3*4+(5/6)'
def brackets_ok(expression):
    q_oper = queue.LifoQueue()
    last_in_lst = []

    brac_dic ={'(':')','{':'}','[':']'}
    lst_brac = [brac for brac in brac_dic.keys()]+[brac for brac in brac_dic.values()]
    for num in expression:
        if num in lst_brac:
            if num in brac_dic.keys():
                q_oper.put(num)
                last_in_lst.append(num)
            elif brac_dic[last_in_lst[-1]] == num:
                q_oper.get()
                last_in_lst.pop(-1)
            else:
                # print(last_in_lst)
                # print(brac_dic[last_in_lst[-1]])
                # print(num)
                return False
    if q_oper.empty():
        return True#True if brackets in expression are ok of False otherwise
    else:
        return False

print(brackets_ok(expression1))
print(brackets_ok(expression2))
print(brackets_ok(expression3))
