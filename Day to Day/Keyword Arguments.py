def parrot(voltage=200, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot()
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                   # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2       keyword arguments       
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments in a different order
parrot('a million', 'bereft of life', 'jump')        # 3
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# here all default values are used as fall back when no argument is passed for that parameter.
# parrot()                     # 4 defaults
# parrot(voltage=5.0)          # 1 positional argument
# parrot(action='VOOOOOM')     # 1 keyword argument
# parrot(type='dead')         # 1 keyword argument

# *args means that there is a variable number of non-keyword arguments and **kwargs means that there is a variable number of keyword arguments.
# for example, *args is positional arguments like parrot(1000) passing value to first positional parameter 
# and **kwargs is keyword arguments like parrot(voltage=1000) passing value to voltage parameter.
# while positional value matters sequence of arguments matters in case of *args but in case of **kwargs sequence of arguments does not matter as we are passing value to specific parameter.
# kwargs are often used when you want to handle named arguments that you have not defined in advance. This allows you to write functions that can accept any number of keyword arguments, which can be useful for handling optional parameters or for passing a variable number of arguments to a function.