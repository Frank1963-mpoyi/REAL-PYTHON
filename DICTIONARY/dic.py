# dictionary is similar to a list in that it is a collection of objects.


'''
Dictionaries and lists share the following characteristics:

Both are mutable.
Both are dynamic. They can grow and shrink as needed.
Both can be nested. A list can contain another list. A dictionary can contain another dictionary. A dictionary can also contain a list, and vice versa.
Dictionaries differ from lists primarily in how elements are accessed:

List elements are accessed by their position in the list, via indexing.
Dictionary elements are accessed via keys

'''

boys = {
    'mpoyi': 'tshibuyi',
    'kanana': 'tshibuyi',
    'mukuna': 'tshibuyi',
    'mutombo': 'tshibuyi',
    'tshibuyi': 'tshibuyi',
    'majondu': 'tshibuyi',
    'kapembu': 'tshibuyi',
    'other': 'none'
}

print(boys)

a = boys["mpoyi"]# we access the value by the key 
b= boys.get("kanana")
print(f'{b} this to get kanana name')

# update a dictionary 
# If you want to update an entry, you can just assign a new value to an existing key
boys['mpoyi']= "Tshibuyi Mulaya Luendu" # dont put in variable
print("\n")
print(f"{boys} Update dict")

# To delete an entry, use the del statement, specifying the key to delete
print("\n")
del boys["other"]
print(f"{boys} delete")

# undefine key raise error 
#print(boys['toronto'])

# access by index raise an error 
#print(boys[1])


# you can use numeric as key and will access it as a key not a index
integer_ = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
print(integer_.get(1))

#   if you want to build a dictionary on the fly
# just built an empty dictionary
empty_ = {} #it s a valid dictionary you can populate it later
empty_['firstname']= 'mpoyi'
empty_['lastname']= 'kanana'
empty_['children'] = ['Ralph', 'Betty', 'Joey']
empty_['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
# empty_['firstname']= 'tshibuyi'# note the
# empty_['firstname']= 'majondu'
# empty_['firstname']= 'kapembu'

print(f"{empty_} dictionary build on the fly ")

#Retrieving the values in the sublist or subdictionary requires an additional index
sub= empty_['children'][-1]
print(sub)

#
sub_dic = empty_['pets']['cat'] 
print(sub_dic)


#Just as the values in a dictionary don’t need to be of the same type, the keys don’t either
foo = {42: 'aaa', 2.78: 'bbb', True: 'ccc'}


# with  dict() method you can also construct a dictionary 

#list of tuple can turn in dictionary 
boys= [('mpoyi','tshibuyi'), ('kanana','tshibuyi'), ('mukuna','tshibuyi'), ('mutombo','tshibuyi'), ('tshibuyi','tshibuyi'), ('majondu','tshibuyi'), ('kapembu','tshibuyi')]

d = dict(boys)

print(d)

""" 1. Restrictions on Dictionary Keys """
'''
Almost any type of value can be used as a dictionary key in Python. 
You just saw this example, where integer, float, and Boolean objects are used as keys
'''

foo = {42: 'aaa', 2.78: 'bbb', True: 'ccc'}

#You can even use built-in objects like types and functions:
d_ = {int: 1, float: 2, bool: 3}


'''
However, there are a couple restrictions that dictionary keys must abide by.

First, a given key can appear in a dictionary only once. Duplicate keys are not allowed. A dictionary maps each key to a corresponding value, so it doesn’t make sense to map a particular key more than once.

You saw above that when you assign a value to an already existing dictionary key, it does not add the key a second time, but replaces the existing value:


'''

#Similarly, if you specify a key a second time during the initial creation of a dictionary, the second occurrence will override the first
MLB_team = {
        'Colorado' : 'Rockies',
        'Boston'   : 'Red Sox',
        'Minnesota': 'Timberwolves',
        'Milwaukee': 'Brewers',
        'Seattle'  : 'Mariners',
        'Minnesota': 'Twins' # this will override the first key
    }

# python key must be immutable like tuple, string etc... 
d = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}


# list and dictionary they can not be a key beacause all of them are mutable
#d = {[1, 1]: 'a', [1, 2]: 'b', [2, 1]: 'c', [2, 2]: 'd'}not allowed


""" 2. Restrictions on Dictionary Values """
# there are restriction on dictionary value can be any type of object mutable or immutable

