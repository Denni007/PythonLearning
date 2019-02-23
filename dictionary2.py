fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
fishdog = {**fish, **dog}



import itertools

option = {
    "x" : ["a","b"],
    "y" : [10,20,30]}
keys = option.keys()
values =(option[key] for key in keys)
comb = [dict(zip(keys,  combination)) for  combination in itertools.product(*values)]
print(comb)
