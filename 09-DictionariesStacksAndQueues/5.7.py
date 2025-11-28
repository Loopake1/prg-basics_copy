def hotel_list(hotels):
    return ','.join([hotel['name'] for hotel in hotels])

def avg_price(hotels):
   return sum([hotel['price'] for hotel in hotels])/len(hotels)
    
hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]
hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]
ttl_avr = (avg_price(hotels_in_Krakow)+avg_price(hotels_in_Sopot))/2

print(ttl_avr,'price')
print(hotel_list(hotels_in_Krakow))
print(hotel_list(hotels_in_Sopot))
if avg_price(hotels_in_Krakow)>avg_price(hotels_in_Sopot):print('Hotels in sopot are cheaper')
else:print('Hotels in krakow are cheaper')
