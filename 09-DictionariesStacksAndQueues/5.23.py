import requests
import json
import datetime

start_date=(datetime.datetime.now()-datetime.timedelta(days = 10)).strftime('%Y-%m-%d')
end_date = datetime.datetime.today().strftime('%Y-%m-%d')
print(start_date,end_date)

euro_dict = {}
euro_lst = []
url = f'https://api.nbp.pl/api/exchangerates/rates/C/EUR/{start_date}/{end_date}?format=json'
response = requests.get(url).content
json_respone =json.loads(response)
for data in json_respone['rates']:
    print(data)
    euro_dict = {}
    euro_dict['Date'] = data['effectiveDate']
    euro_dict['Buying_rate'] = data['bid']
    euro_dict['Selling_rate'] = data['ask']
    euro_lst.append(euro_dict)
json.dump(euro_lst,open('09-DictionariesStacksAndQueues/euro.json','w'),indent=4)
print('Date            Buying Rate     Selling Rate')
print('============================================')
for euro_data in euro_lst:
    print(f"{euro_data['Date']}        {euro_data['Buying_rate']}          {euro_data['Selling_rate']}")
    
    # print(data['table'],data['rates'][0]['effectiveDate'])
# table A of middle exchange rates of foreign currencies,
# table B of middle exchange rates of foreign currencies,
# table C of buy and sell prices of foreign currencies;