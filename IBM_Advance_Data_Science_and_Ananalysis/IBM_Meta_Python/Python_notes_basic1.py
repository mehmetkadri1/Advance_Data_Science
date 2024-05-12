L=['michacel Jackson', 10.1, 1982]
L.extend(['pop,',10])
L.append('M')
del(L[3])
print(L)
L.remove(10) #difference between del and remove method is you can specify exact element which you want to delete in list with remove method  
print(L)
print(L[::2])

"""A dictionary is a collection of key-value pairs.
Each key is unique within the dictionary, and it is used 
to access its associated value.
A list is an ordered collection of items.Each item in 
list has an index, starting from 0 for the first item
"""
#Creating new dictionary:
dict_new={}
person={'name':'john', 'age':30, 'city':'new york' }

item_list=list(person.items())
value_list=person.values()
key_list=person.keys()
person.update({'age':25})
del(person['city'])
person['county']='UK'
print(person)



