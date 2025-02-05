#DAY 1

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

for i in range(10):
    if(i == 5):
        continue
    print(i)
print("rest of the code")