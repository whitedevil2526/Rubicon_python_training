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