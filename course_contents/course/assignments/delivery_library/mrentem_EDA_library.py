


## FUNCTION WHICH CREATES A DATAFRAME OF A PARTICULAR FORM:

def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {c: [str(c) + str(i) for i in ind]
            for c in cols}
    return pd.DataFrame(data, ind)


## CLASS THAT ALLOWS US TO DISPLAY MULTIPLE DATAFRAMES SIDE BY SIDE

class display(object):
    """Display HTML representation of multiple objects"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""
    def __init__(self, *args):
        self.args = args
        
    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                         for a in self.args)
    
    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)
    


## FUNCION PARA CREAR MULTI INDICES EN DATASETS JERARQUIZADOS ---> Tidy format

def jerarquizar_multi_indice(data, lista1, lista2):
    """ funcion para crear un multi indice de dos niveles que establezca
    una jerarquia a partir de listas. Nos proporciona un dataset en formato tidy que 
    puede ser util para emplear en herramientas BI. data = set de datos; lista1 = primer nivel
    de la jerarquia; lista2 = segundo nivel de la jerarquia"""

    index = pd.MultiIndex.from_product([lista1, lista2])
    data.index.names = ['lista1', 'lista2']
    data = data.sort_index()
    return data

    """ TODO revisar que funcione con algun set """


## verify_integrity FLAG: RAISES A MESSAGE WHEN THE INDEX IS REPEATED AFTER A CONCATENATION

try:
    pd.concat([x, y], verify_integrity=True)
except ValueError as e:
    print("ValueError:", e)


## GROUP ITERATION TO SEE THE SHAPE OF THE GROUPS

def group_shape(df):

    for (column, group) in df.groupby('column_name'):
        print("{0:30s} shape={1}".format(column, group.shape))



####################################################################
## DECORATORS   ###################################################
###################################################################

# A few decorators: https://realpython.com/primer-on-python-decorators/#timing-functions

## DECORATOR TO CALCULATE HOW MUCH TIME IN FUNCTION EXECUTION:


# importing libraries 
import time 
import math 
  
def calculate_time(func): 
      
    # added arguments inside the inner1, 
    # if function takes any arguments, 
    # can be added like this. 
    def inner1(*args, **kwargs): 
  
        # storing time before function execution 
        begin = time.time() 
          
        func(*args, **kwargs) 
  
        # storing time after function execution 
        end = time.time() 
        print("Total time taken in : ", func.__name__, "is... ", end - begin, " seconds") 
  
    return inner1 
 

# this can be added to any function present, in this case to calculate a factorial 
@calculate_time
def factorial(num): 
  
    # sleep 2 seconds because it takes very less time 
    # so that you can see the actual difference 
    time.sleep(2) 
    print(math.factorial(num)) 
  
# calling the function. 
factorial(9510)
  
## DEBUGGING CODE

import functools

def debug(func):
    """Print the function signature and return value.
    The decorator will print the arguments a function is called with as well as 
    its return value every time the function is called"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug


## SLOWING DOWN CODE:

import functools
import time

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)


## REGISTERING PLUGINS

import random
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)

## USER LOGGED IN:

from flask import Flask, g, request, redirect, url_for
import functools
app = Flask(__name__)

def login_required(func):
    """Make sure user is logged in before proceeding"""
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required

@app.route("/secret")
@login_required
def secret():
    ...




################################################################

# Things to think about and develop code for. Maybe not worth as could be packages solving the issue


def partition_datasets():
    """ TODO Function to quickly partition datasets as a sort strategy using FANCY INDEXING 
    (e.g. to split a set of values for validation) 
    """




import numpy as np

def selection_sort(x):
    """ TODO function to make a simple selection sort repeatedly finds the minimum value from a list, 
    and makes swaps until the list is sorted (ver numpy2 file)
    """ 
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x



def bogosort(x):
    while np.any(x[:-1] > x[1:]):
        np.random.shuffle(x)
    return x
