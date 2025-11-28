import json
vote_dict = {}
vote_person= 1
while True:
    vote_person = input('Enter name for voting candidate or press enter to finish: ')
    if vote_person == '':
        break
    if vote_person not in vote_dict:
        vote_dict[vote_person] = 1
    else:
        vote_dict[vote_person]+=1
json.dump(vote_dict,open('09-DictionariesStacksAndQueues/voting.json','w'),indent=4)