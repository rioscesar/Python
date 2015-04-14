def check_arguments(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            return "Something went wrong!"
    return helper

@check_arguments
def myFunc(x):
    return x / x
    

print(myFunc(6))
    
