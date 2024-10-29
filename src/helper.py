import random as r
import re

# verifies if a, b are decimal values, otherwise False
def inputValidation(a,b):
    a, b = str(a), str(b)
    pat = '^[0-9]$'
    ret_flag = re.match(pat,a) and re.match(pat,b)
    return ret_flag
    
# generates a string integer of a float, otherwise "-1"
def genInt(start=1,stop=6):
    dec_flag = inputValidation(start,stop)
    str_int = str(r.randint(start,stop)) if dec_flag else "-1"
    return str_int
    
# generates a string of a float, otherwise "-1"
def genFloat(start=0,stop=100):
    my_int = genInt()
    int_check = my_int != "-1"
    sig_fig = "." + str(r.randint(start,stop))
    str_float = my_int + sig_fig if int_check else "-1" 
    return str_float

# return a float grade
def genGrade():
    return float(genFloat())
