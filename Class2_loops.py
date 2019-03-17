for x in range(10):
        print(x)

print("-----------------------------------------")
# 1 is the initial value of y, 5 is the number y has to be smaller than to continue loop
for y in range(1, 5):
        print(y)

print("-----------------------------------------")
# 2 is the increment increase in each iteration
for z in range(1, 20, 2):
        print(z)

print("-----------------------------------------")
num = 1
while num <= 15:
        print(num)
        num += 1
#        num=num+1

print("-----------------------------------------")
count = 1
while 1 > 0:
        print(count)
        count +=1
        if count == 3:
                break
# (I can also use break in a for loop)

print("-----------------------------------------")
count = 0
while count < 8:
        count +=1
        if count == 3:
                continue
        print(count)

print("-----------------------------------------")
n = 0
while n < 5:
        print (n)
        n +=1
else:
        print ("while loop is now over. we will see this only if we entered the loop")