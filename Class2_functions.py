#vars
gv1 = "global variable"

#this funtion prints a variable
def printMyName():
        print("Ayala")
#this function returns a value into the main module
def f1():
    return "f1 returned from function"
#this function gets a value from the main module
def f2(var):
    print(var)
#this function returns the phrase Hello with the name that is an input from the main module
def f3(name):
    return "Hello "+ name
#this function gets 3 arguments
def f4(a,b,c):
    d=a+b+c
    return d
#this function uses a global variable
def f5():
    return gv1

if __name__ == '__main__':
    printMyName()
#setting the value that's returned from f1 into x and then printing x
    x=f1()
    print (x)
#running function f2 and sending a value into it
    f2("input value to f2")
#sending a value to function f3 and then setting the output of f3 in a variable and printing that variable
    f3_output=f3("Ayala")
    print(f3_output)
#sending 3 variables to function f4 and printing the returned value
    f4_result=f4(1,2,3)
    print(f4_result)
#sending a value into f5 that returns a global variable
    x=f5()
    print (x)