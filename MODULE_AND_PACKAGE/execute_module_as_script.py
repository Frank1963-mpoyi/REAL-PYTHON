'''
Executing a Module as a Script
Any .py file that contains a module is essentially also a Python script, 
and there isn’t any reason it can’t be executed like one.

'''

s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]

def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass

#This can be run as a script:
# open CMD :
#C:\Users\MPOYI TSHIBUYI\Documents> navigate to the directory where is python file.py
#C:\Users\MPOYI TSHIBUYI\Documents>python working_hours.py # after driving in the directory type python first plus the file name


'''
When a .py file is imported as a module, Python sets the special dunder 
variable __name__ to the name of the module. However, if a file is run 
as a standalone script, __name__ is (creatively) set to the string '__main__'. 
Using this fact, you can discern which is the case at run-time and alter behavior 
accordingly:


'''