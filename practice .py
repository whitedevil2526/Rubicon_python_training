#DAY 1
#string

#a=10
#b=20
#c=a+b
#print(c)

a=5
b=2
c = a==b
print(c)

a=5
b=2
c=3
d=200
print(a>b and a>c)
print(a>b and a<c)
print(a<b and a>c)
print(a<b and a<c)
print(not(a<b))
print(not(a>b))

#assignment operator

a=10
b=20
m=15
y=a + b + m
print(y)

m+= 10
print(m)

m-= 10
print(m)

m*= 10
print(m)

m/= 10
print(m)

#in operator

st1="welcome to grreyshows"
print("to" in st1)
print("subs" in st1)

#not operator
st1="welcome to grreyshows"
print("to" not in st1)

#is operator
a=10
b="10"
print(a is b)

#operator precedency
value = (1+1)*2**4//3+4-1
print(value)

#implicit conversion
j="hello" + " "
k="geeky shows "
p=j + k
print(p)

w='10'
e='10'
r=w + e
print(r)

#explicit conversion
q=10
u='10'
print(type(u))
r=q + int(u)
print(r)

#variable store output
date=[10,20,-30,21.3,"hello"]
print(date)
print("welcome", end=" ")
print("to", end=" ")
print("geekyshow")

#variable store input
name= input("enter your name: ")
print(name)
print(type(name))

num=int(input("enter your number:"))
print(num)
print(type(num))

nm=input("enter your name:")
print("your name is",nm)

#escape sequence
print("welcome to \"Hello world\"")
print("welcome to \'Hello world\'")

#if statement
if 5>2:
    print("it is greate")

#if statement with group of statement
if 5>2:
    print("greater")
    print("5 is greater then 2")
    if(6<2):
        print("6 is greeater than 2")
print("rest of the code")

#if else
a=int(input("enter number greater than 2 :"))
if(a > 2):
    print("you have entered:",a)
else:
    print("the number is less than 2")

a=int(input("enter number greater than 2:"))
b=10000
if(a <= b):
    print("correct!! you have entered:",a)
else:
    print("warning!! your balance is insufficient:",a)
    print("your balance is:",b)

#elif
a=10
b=20
if a>b:
    print("a is grater than b")
elif a==b:
    print("a is equal to b")
elif a<b:
    print("a is less than b")

#while loop
a=2
while a<=20:
    print(a)
    a+=2
print("rest of the code")

i=0
while True:
    i+=1
    print(i)
    if(i == 5):
        break
print("rest of the code")

#nested while loop
i=1
while i<=3:
    print("outer loop",i)
    i+=1
    j=1
    while j<=5:
        print("inner loop",j)
        j+=1
print("rest of the code")

#range function

print("range  with stop")
a=range(5)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

c=range(-1,-10,-2)
print(c[0])
print(c[1])
print(c[2])
print(c[3])

c=range(-10,-1,2)
print(c[0])
print(c[1])
print(c[2])
print(c[3])

c=range(5,0,-1)
print(c[0])
print(c[1])
print(c[2])
print(c[3])
print(c[4])

c=range(0,5,1)
print(c[0])
print(c[1])
print(c[2])
print(c[3])

#for loop
st="geekyshows"
y=len(st)
print(y)
for ch in range(y):
    print(ch,"=",st[ch])

st="geekyshows"
y=len(st)
print(y)
i=0
while(i<y):
    print(i,"=",st[i])
    i+=1
print("rest of code")

a= range(5)
for i in a:
    print(i)

b=range(10)
for i in b:
    print(i)

st="GeekyShows"
for ch in st:
    print(ch)

for i in range(3):
    print("outer loop",i)
    for j in range(5):
        print("inner loop",j)
print("rest of the code")

#continue
for i in range(10):
    if(i == 5):
        continue
    print(i)
print("rest of the code")

#pass statement
for i in range(10):
    if(i == 5):
        pass
    print(i)
print("rest of the code")

#memory allocation
str1="steekyshows"
str2="Geekyshows"
str3="python"
str4=str3
print("str1",str1,id(str1))
print("str2",str2,id(str2))
print("str3",str3,id(str3))
print("str4",str4,id(str4))

#comparing string

#fstring 
a=10
b=20
print(f"{a}")
print(f"{a} {b}")
print(f"{b} {a}")

a="samarth"
print(f"{a[::-1]}")

st="RACECAR"
str1= st[::-1]
print(str1)
if(st == str1):
    print("palindrome")
else:
    print("not palindrome")

#example 

name="hello world"
str1=name.upper()
str2=name.title()
str3=name.capitalize()
str4=name.isupper()
str5=name.isdigit()
str6=name.isalpha()
str7=name.isalnum()
str8=name.lstrip()
print(name)
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
print(str7)
print(str8)

name="Geeky-shows"
old="Geeky"
new="New"
a=('hello','how','are','you')
b="Hi How Are You"
str1=name.replace(old,new)
str2=name.split('-')
str3=" ".join(a)
str4=name.startswith('Hi')
str5=name.endswith('ye')
print(name)
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)

def issubsequence(string, substring):
    i=0
    j=0
    while i< len(substring) and j< len(string):
        if substring[i] == string[j]:
            i += 1
        j +=1
    return i == len(substring)

string="abcdefghi"
substring="adi"
result = issubsequence(string,substring)
print(result)


def issubsequence(string, substring):
    a=0
    b=0
    while a>len(substring) and b>len(string):
        if substring[a] == string[b]:
            a +=1
        b+=1
    return a == len(substring)

string="classmate"
substring="cla"
result = issubsequence(string,substring)
print(result)

text="samarthsabale"
if not text:
    print("empty string")
else:
    for char in text.lower():
        if char in("a","e","i","o","u"):
            print(f"{char} is a vowel")
        elif not char.isalpha():
            print(f"{char} is not a lette")
        else:
            print(f"{char} is a consonant")

month="february"
month_31_days =("janurary","march","may","july","August","october","december")
month_30_days = ("april","june","september","november")

if month in month_31_days:
    print(f"{month} has 31 days")
elif month in month_30_days:
    print(f"{month} has 30 days")
else:
    print(f"{month} has 28 days")

a=3
b=2
c=1

if a> b> c:
    print("decreasing order")
elif a < b < c:
    print("increasing order")
else:
    print("number is neither increasing or decreasing")

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if year % 100 ==0:
            if year % 400 == 0:
                leap = True
        else:
            leap= True
    
    return leap

year = int(input())
print(is_leap(year))