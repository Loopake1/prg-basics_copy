import json
file_name= "09-DictionariesStacksAndQueues/favourite.json"
book_dic = {'name':'That Spoke Zarathustra',"Author":"Friedrich Nietzsche",'Release date':'1883'}
json.dump(book_dic,open(file_name,'w'),indent=4)