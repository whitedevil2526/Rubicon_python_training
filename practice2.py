#DAY 2
#list

a=[10,20,-50,21.3]
print(a[1])
print(a[2:3])
a[1]=40
print(a[1])
print(a,id(a))

a=[10,20,21.3,-50]
n=len(a)
i=0
while i< n:
    print(i,"=",a[i])
    i+=1
del a[1]
print(a)

a=[10,20,-50,21.3]
print("before appending:")
for element in a:
    print(element)
a.append(100)
print()
print("after appending:")
for element in a:
    print(element)


a = ['geeks', 'for']
b = [6, 0, 4, 1]
# Add all element of 'b' at the end of 'a'
a.extend(b)
print(a)


a = ['geeks', 'for']
# Append 'geeks' at the end of 'a'
a.append('geeks')
print(a)
# Append an entire list to 'a'
a.append(['a', 'coding', 'platform'])
print(a)

a=[]
n=int(input("enter number of element:"))
for i in range(n):
    a.append(int(input("enter element:")))
print(a)

for element in dir(list):
    if "__" in element:
        pass
    else:
        print(element)

a=[10,20,30,10,90,"Geekyshows"]
print("before:",a)
a.insert(3,"subscribe")
print("after:",a)

a=[10,20,30,10,90,"Geekyshows"]
print("before pop:",a)
a.pop(3)
print("after pop:",a)

a=[10,20,30,10,90,"Geekyshows"]
print("before pop:",a)
a.pop()
print("after pop:",a)

a=[10,20,30,10,90,"Geekyshows"]
print("before remove:",a)
a.remove(10)
print("after remove:",a)

#remove element from list and covert it into number
a= [9,5,4,3,8,5,7]
print("before remove:",a)
a.remove(5)
print("after remove",a)
number1= int("".join(map(str, a)))
print("number is:",number1)
a.insert(1,5)
print("after inserting:")
a.pop(5)
print("element after pop:",a)
number2= int("".join(map(str, a)))
print(number2)
if(number1>number2):
    print("grater number is:",number1)
else:
    print("greate number is:",number2)