""" The Importance of Python Functions """

# Abstraction and Reusability

# you make a code and you want to use the same code in different files
# you will just copy and paste and later on you find out that you must modify that code
# you will go every where you pasted to modify the code that is a big job 

# the solution to this is making python function 
# if you change one location the change will be pick up everywhere you call that function 


"""  Modularity  """

# Main program

# Code to read file in
# <statement>
# <statement>
# <statement>
# <statement>

# Code to process file
# <statement>
# <statement>
# <statement>
# <statement>

# Code to write file out
# <statement>
# <statement>
# <statement>
# <statement>

#NOTE: instead putting the comment to describe the codee title we can 
# have the function and name it 

def read_file():
    # Code to read file in
    # <statement>
    # <statement>
    # <statement>
    # <statement>
    pass

def process_file():
    # # Code to process file
    # <statement>
    # <statement>
    # <statement>
    # <statement>
    pass

def write_file():
    # # Code to write file out
    # <statement>
    # <statement>
    # <statement>
    # <statement>
    pass


# Main program
read_file()
process_file()
write_file()


"""  Namespace Separation  """
# the same variable name use outside the function can also be used inside the function
# or the same variable can also be used in other function 
# you can use any name without worried if it was used or not 

#when a Python function is called, a new namespace is created for that function, one that is distinct from all other namespaces that already exist
