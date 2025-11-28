prov_file = list(open('09-DictionariesStacksAndQueues/province.csv','r').read().split('\n')[1:-1])
veh_file  = open('09-DictionariesStacksAndQueues/vehicle.txt','r').read().split('\n')[:-1]
num_prov_veh = {}
prov_dict = {line.split(',')[0]:line.split(',')[1] for line in prov_file}
for veh_num in veh_file:
    if prov_dict[veh_num[0]] not in num_prov_veh:
        num_prov_veh[prov_dict[veh_num[0]]] = [veh_num]
    else:
        num_prov_veh[prov_dict[veh_num[0]]].append(veh_num)
print(num_prov_veh['Podlaskie'])
