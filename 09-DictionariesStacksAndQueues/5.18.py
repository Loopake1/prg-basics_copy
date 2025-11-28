import json
dogs_file =json.load( open('09-DictionariesStacksAndQueues/dogs.json','r'))


for dog in dogs_file:
    if dog['age']<5:
        for dog_info in dog:
            print(f"{dog_info}:{dog[dog_info]}")
        print()