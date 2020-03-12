import collections


""" 0. Creating dictionaries """
dict_1 = {'a': 1, 'b': 2}
dict_2 = {'c': 3, 'a': 4}

""" 0.1 Creating a single dictionary """
res = collections.ChainMap(dict_1, dict_2)

""" 1. Output All key-values with new common dictionary """
print("\n\t\t***** Output the Elements of new Map *****")
print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))
for k, v in res.items(): print("{} = {};".format(k, v), end=' ')

# Finding a specific value in the result
print("\n\n\t# - check if some element in the map ")
print("<a> in res: {}".format(('a' in res)))
print("<b> in res: {}".format(('b' in res)))
print("<c> in res: {}".format(('c' in res)))
print("<d> in res: {}".format(('d' in res)))

""" 2. Changing Map Order """
res_1 = collections.ChainMap(dict_1, dict_2)
res_2 = collections.ChainMap(dict_2, dict_1)
print("\n\t\t***** Visualisation of Changing Map Order *****")
print("Order <dict_1>, <dict_2>  : ", res_1.maps)
print("Order <dict_2>, <dict_1>  : ", res_2.maps)


""" 3. Map Updating """
days_1 = {'day1': 'Mon', 'day2': 'Tue'}
days_2 = {'day3': 'Wed', 'day4': 'Thu'}

res = collections.ChainMap(days_1, days_2)
print("\n\t\t***** Visualisation of Map Updating *****")
print("ChainMap BEFORE updating  : ", res.maps)         # Checking ChainMap status
days_2['day4'] = 'Fri'  # Updating some Value
print("ChainMap AFTER updating  : ", res.maps)         # Notice, that element has been changed in ChainMap!

