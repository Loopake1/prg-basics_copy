paragraph = "cat dog mouse cat rat cat mouse".split(' ')
par_dict = {}
for word in paragraph:
    if word not in par_dict.keys():
        par_dict[word] = 1
    else:
        par_dict[word]+=1
print(par_dict)