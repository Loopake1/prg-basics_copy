import json
file = json.load(open('09-DictionariesStacksAndQueues/reservations.json','r'))
print(f"Number of rooms {len(file['reservations'])}")
print(len([paid_room for paid_room in file['reservations'] if paid_room['paid']]),'number of paid reservations')
print(len([paid_room for paid_room in file['reservations'] if paid_room['paid'] == False]),'number of unpaid reservations')
print(sum([paid_room['price_per_night'] for paid_room in file['reservations'] if paid_room['paid']]),'total value of paid reservations')
print(sum([paid_room['price_per_night'] for paid_room in file['reservations'] if paid_room['paid'] == False]),'total value of unpaid reservations')

