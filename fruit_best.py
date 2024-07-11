name_list = []
value_list = []
value_lis = {}
frots = ({'name':'sib','shape':'sphere','mass':350,'volume':120},
        {'name':'anbe','shape':'morabae','mass':150,'volume':120},
        {'name':'limo','shape':'sphere','mass':150,'volume':100},
        {'name':'sib','shape':'sphere','mass':500,'volume':250})
def fruits(frt_tpl):
    for frot in range(len(frt_tpl)):
        rule1_1 = frt_tpl[frot]['shape'] == ('sphere')
        rule1_2 = frt_tpl[frot]['mass'] >= 300
        rule2_1 = frt_tpl[frot]['mass'] <= 600 
        rule2_2 = frt_tpl[frot]['volume'] >= 100
        rule3 =frt_tpl[frot]['volume'] <= 500
        if rule1_1 and rule1_2 and rule2_1 and rule2_2 and rule3:
            print(frt_tpl[frot])
    for i in frt_tpl:
        names = i['name']
        name_list.append(names)
    print('\n')    
    for name in name_list:
        value_list.append(name)
        for val in value_list:
            value_lis.setdefault(val , name_list.count(val))
        if value_list.count(name) == 2:
            value_list.remove(name)
    print(value_lis)
    
fruits(frots)