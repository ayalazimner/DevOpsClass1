print ("----Questions 1 + 2 ----")
try:
    a= 1/0;
except ZeroDivisionError as err:
    print ("Can't divide by zero: ",err)

print ("----Question 7----")
file_words=open("D:\Python\Test Files\Words.txt", 'w')
file_words.close()

print ("----Question 8----")
file_words=open("D:\Python\Test Files\Words.txt", 'a')
file_content=file_words.write("Ayala")
file_words.close()

print ("----Question 9----")
file_words=open("D:\Python\Test Files\Words.txt", 'r')
file_content=file_words.read()
file_words.close()
print(file_content)

print ("----Question 10----")
file_words=open("D:\Python\Test Files\Words.txt", 'a', encoding='utf-8')
heb_content=file_words.write("\nעברית, עברית, עברית")
file_words.close()
file_words=open("D:\Python\Test Files\Words.txt", 'r', encoding='utf-8')
heb_content=file_words.read()
print(heb_content)
file_words.close()

print ("----Question 11----")
from PIL import Image
img = Image.new('RGB', (60, 30), color='red')
img.save('D://Python//Test Files//image1.jpg')