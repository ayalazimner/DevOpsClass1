#default is opening the file for reading and in text mode:
#my_file=open("D:\Python\Test Files\MyName.txt")
#open for reading and updating:
# my_file=open("D:\Python\Test Files\MyName.txt", 'r+')
# content=my_file.read()
# print(content)
# my_file.close()
# my_file=open("D:\Python\Test Files\MyName.txt", 'a')
# content=my_file.write("\nadd this text")
# my_file.close()
# my_file=open("D:\Python\Test Files\MyName.txt")
# content=my_file.read()
# print(content)
# my_file.close()



#Write and Read Hebrew file

# my_file2=open("D:\Python\Test Files\Heb.txt", 'a', encoding='utf-8')
# content2=my_file2.write("\nעוד עברית")
# my_file2.close()
# my_file2=open("D:\Python\Test Files\Heb.txt", 'r', encoding='utf-8')
# content2=my_file2.read()
# print(content2)
# my_file2.close()

#I will use try/except when the code is doing something out of my control - unexpected input, referencing a file or a server.
#general exception
try:
    my_file=open("D:\labla.txt")
    content=my_file.read()
    print(content)
    my_file.close()
except:
    print ("error is handled")

#i/o exception, I can referencd different types of errors according to error type
try:
    my_file=open("D:\labla.txt")
    content=my_file.read()
    print(content)
    my_file.close()
except IOError as err:
    print ("i/o error: can't read data. Error: ",err)
except ValueError:
    print ("there is a value error")
print("program continues")

#finally will always run, we can put it after try or after exepct
try:
    my_file=open("D:\labla.txt")
    content=my_file.read()
    print(content)
    my_file.close()
except IOError as err:
    print ("i/o error: can't read data. Error: ",err)
finally:
    print ("finally will run anyway")
#in this case the exception will stop the program, but I will use this when I want my code to fail in case of the exception. In addition, I want stuff to happen like close a file.
# try:
#     my_file=open("D:\labla.txt")
#     content=my_file.read()
#     print(content)
#     my_file.close()
# finally:
#     print ("finally will run anyway even if there's an exepction")

#Debugger: need to add a breakpoint one row before the code line we suspect, I can add severan breakpoints and click resume or have 1 breakpoint and use step-over to go each row
x=1
x=2
x=3
x=4
x=5
y=x+6
print(y)

#evaluate expression: change values while running without changing the code, during debugger run. right click the program during debugger > evaluate exception.
#Add to watches: this will add the variable to wathes during debugging, so I can track the value of a variable during debug

#pip - package management system: will search for folders and modules from PyPI
#import can only work with modules which are saved locally on my computer. If I don't have it then I need to search for the package and save it first.


