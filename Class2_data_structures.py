#--------Array
# i is always integer, c is char
import array as arr
a = arr.array("i",[4,5,6,7,8,9])
print (a)
#setting the value 0 in index 0
a[0] = 0
#printing the value in index 0
print (a[0])
#adding an additional element to the array
a.append(111)
print (a[6])
#removing an element from the array in index 2
a.pop(2)
print (a)
#adding an element in specific index 1
a.insert(1,222)
print (a[1])

#get the length of an array
print ("length: " , len(a))

#print all elements in an array without using index
for temp in a:
        print(temp)

# print all elements in an array with using index
for x in range (len(a)):
    print (a[x])

# --------List: can contain all data types
list1 = [5,"vstr",True]
print(list1[2])

#we will use an array and not a list when we know which data type i'll have. using an array saves processing time of checking the data type of each element.

# --------Tuple: the number of elements is known in advance and also the values in it (completely read only), we cannot change the number. can be written in one of these options:
tpl_1 = 1,2,3,4,5
tpl_2 = ('a','b',3)
print (tpl_1, tpl_2)
print ("value in tuple 1 in index 2 is: " ,tpl_1[2])

# --------Dictionary: Key = Value
dictionary1 = {'A': 1, 'B': 2}
#set the value 5 in the key A
dictionary1['A'] = 5
#print dictionary keys
print(dictionary1.keys())
#print dictionary values
print(dictionary1.values())
#delete disctionary key
del(dictionary1['A'])
print(dictionary1.values())
