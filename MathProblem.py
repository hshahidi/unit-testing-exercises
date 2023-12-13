#production code
def add_num(u, v):                     
    return u + v                      

def multiply_num(j, k, l):
    return j * k * l                  

def divide_num(x, y):
    return x / y

def combine_results(a, b, c):
    return divide_num(add_num(a, c), multiply_num(a, b, c))

#biz req, input: list of numbers 25 inputs, like wafer yields; output lot avg of wafer yield
