'''
Python Packages
Suppose you have developed a very large application that includes many modules. 
As the number of modules grows, it becomes difficult to keep track of them all if 
they are dumped into one location. This is particularly so if they have similar 
names or functionality. You might wish for a means of grouping and organizing them.

Packages allow for a hierarchical structuring of the module namespace using dot notation. 
In the same way that modules help avoid collisions between global variable names, 
packages help avoid collisions between module names.

Creating a package is quite straightforward, since it makes use of the operating system’s 
inherent hierarchical file structure. Consider the following arrangement:



Package Initialization
If a file named __init__.py is present in a package directory, it is invoked when the package or a module in the package is imported. This can be used for execution of package initialization code, such as initialization of package-level data.

For example, consider the following __init__.py file:

__init__.py

'''



