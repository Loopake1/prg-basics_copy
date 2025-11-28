import json
file_name= "09-DictionariesStacksAndQueues/product.json"
product = {}
name = input('Enter product name: ')
price =float(f"{float(input('Enter product price: ')):.2f}")
paid = input('Paid yes/no: ').lower() == 'yes'
product['name'] = name
product['price'] = price
product['paid'] = paid
json.dump(product,open(file_name,'w'),indent=4)