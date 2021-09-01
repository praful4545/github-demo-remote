# add implementation
def add(x,y):
    return x+y
#substract implementation
def subtract(x,y):
    return x-y;            #on master branch
# multiply implementation
def multiply(x,y):
    return x*y; #on bug branch

#divide implementation
def divide(x,y):

    if y==0:
        return divideby0error
    else:
        return x/y;           #on master

