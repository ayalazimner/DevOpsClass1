print ("----Question 1----")
print ("Hello")
print ("Ayala")

print ("----Question 2----")
print (1 + 2)

print ("----Question 3----")
import platform
print(platform.python_version())

print ("----Question 4----")
def reverse(string):
    string = "".join(reversed(string))
    return string
s = "hello"
print(reverse(s))

print ("----Question 5----")
word = "python"
print ("number of characters in the string",word,"is:",len(word))

print ("----Question 6----")
import datetime
t = datetime.datetime.now()
print (t)

print ("----Question 7----")
x = 1
y = 2
if x > y:
    print (x)
elif y > x:
    print (y)
else:
    print ("equals")

print("----Question 8----")
if 120 > 5 and 120 < 200:
    print ("Match")