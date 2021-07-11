""" Operators and Built-in Functions"""

# the in , not, not in , work with dictionary 
MLB_team = {
        'Colorado' : 'Rockies',
        'Boston'   : 'Red Sox',
        'Minnesota': 'Twins',
        'Milwaukee': 'Brewers',
        'Seattle'  : 'Mariners'
    }

'Milwaukee' in MLB_team
True
'Toronto' in MLB_team
False
'Toronto' not in MLB_t

MLB_team['Toronto'] # is not in dictionary it will raise an error to avoid this error 
# you can use sort of evaluation with the in operator 
'Toronto' in MLB_team and MLB_team['Toronto']
False

# to know the length of the dictionary 
len(MLB_team) 

