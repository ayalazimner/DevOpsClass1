print# print ("----Question 1----")
x = 1
y = 2
if x > y:
    print ("Big")
elif y > x:
    print ("Small")

print ("----Question 2----")
for i in range (5):
    print (i)
    i = i + 1

print ("----Question 3----")
season = 1
if season == 1:
    print ("summer")
elif season == 2:
    print ("winter")
elif season == 3:
    print("fall")
elif season == 4:
    print("spring")

print ("----Question 4----")
count = 1
while count<11:
    print (count)
    count = count + 1

print ("----Question 5----")
age=34
fl="Z"
ild=3.61
abroad="True"
apt=2
print ("My age is ",age,", The first letter of my first name is ",fl,", IL to USD currency is ", ild,", Did I fly abroad? ",abroad,", I live in apartment ",apt,)
sum=age+ild
print ("Age + Currency = ",sum)

print ("----Question 6----")
phone_number = input("please enter phone number: ")
print ("Phone number is:", phone_number)

print ("----Question 7----")
def printHello():
    print("Hello")
printHello()
def celculate():
    sum=5+3.2
    print(sum)
celculate()

print ("----Question 8----")
def getName():
    my_name=input("Please enter your name: ")
    print("Your name is: ",my_name)
getName()

def divide():
    my_num=float(input("Please enter a number: "))
    new_num=my_num/2
    print("Your number divided by 2 is: ",new_num)
divide()

print ("----Question 9----")
def sum_numbers():
    num1=float(input("Please enter a number: "))
    num2 = float(input("Please enter another number: "))
    sum=num1+num2
    print("Sum of both numbers is: ",sum)
sum_numbers()

def two_strings():
    str1=input("Please enter a phrase: ")
    str2=input("Please enter another phrase: ")
    strings=str1 + " " + str2
    print(strings)
two_strings()

print ("----Question 10----")
import array as arr
a = arr.array("i",[1,3,5])
for a_len in range(len(a)):
        print(a[a_len])

print ("----Question 11----")
for x in range(1,6):
    for y in range (x):
        print("#", end='')
    print ()

print ("----Question 12----")
N = 7
for i in range(N):
    for j in range(N):
        if (i == j) or ((N - j -1) == i):
            print('#', end = '')
        else:
            print(' ', end = '')
    print('')


print ("----Question 13----")
def getNumber():
    my_number=int(input("Please a number: "))
    return my_number

def sumDigits(input_num):
    lst = [int(i) for i in str(input_num)]
    digits_sum = 0
    for x in range(len(lst)):
        digits_sum = digits_sum + lst[x]
    print("The sum of digits in your number is: ",digits_sum)

sumDigits(getNumber())

