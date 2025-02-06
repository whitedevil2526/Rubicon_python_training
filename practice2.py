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

list1=['9','8','7','6','5','4','3','2','1']
r1=map(int,list1)
print(r1)

list1 = ['9', '8', '7', '6', '5', '4', '3', '2', '1']
r1 = map(int, list1)
r1_list = list(r1)
print(r1_list)

list=[10,50,40,90]
list.reverse()
r1=list.index(10)
print(list)
print(r1)

#count
a=[10,20,30,10,40,10]
num=a.count(10)
a.clear()
a.sort()
print(num)
print(a)

list=[101,102,103,104,105,106,107,108]
print("last 4 element")
d=x[-4:-1]
for i in d:
    print(i)
print(d)

#negative index of multiple list
a = [9,5,4,3,6,7,[[12,13,14],[15,16]]]
print(a[-1][-2][-1])
print(a[-1][-2])
print(a[-5])

#list multiplication to print multiple element
a=[1,2,3]
print(a)
result=a*3
print(result)

a=[10,20,30,40]
b=a
print("A",a)
print("B",b)

a=[10,20,30,40]
b=a.copy()
print("A",a)
print("B",b)
print("After modifying:")
a[1]=55
print("A",a)
print("B",b)

#sort() and sorted()
my_list = [5, 2, 9, 1]
my_list.sort()  # In-place sorting
print(my_list)  # Output: [1, 2, 5, 9]
my_tuple = (5, 2, 9, 1)
sorted_tuple = sorted(my_tuple)  # Creates a new sorted list from tuple
print(sorted_tuple)

#simillar list operation 
a=[5,4,3,5,3,9,8,7,6,7]
b= []
for i in range(len(a)):
    if ((a.count(a[i]))==1):
        b.append(a[i])
print(b)

a=[5,4,3,5,3,9,8,7,6,7]
b= []
for i in range(len(a)):
    if ((a.count(a[i]))==2):
        b.append(a[i])
print(b)


#nestedlist 
#modification
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Modify nested list by adding 10 to each element in sub-lists
for i in range(len(nested_list)):
    for j in range(len(nested_list[i])):
        nested_list[i][j] += 10
print(nested_list)

names_score =[['amol',10],['julie',20],['rahul',10],['amit',50],['arjun',40],['ketan',20]] 

scores=[]

for stud in names_score:
    scores.append(stud[1])
scores=sorted(set(scores))
print(scores)
second_lowest=scores[1]
print(second_lowest)
name_second_lowest=[]
for stud in names_score:
    if stud[1] == second_lowest:
        name_second_lowest.append(stud[0])
print(name_second_lowest)