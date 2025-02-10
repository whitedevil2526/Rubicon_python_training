#day 4 dict
my_dict = {"jan":45,"feb":25,"mar":35}
new_key = "april"
new_value = 30

if new_key not in my_dict:
    my_dict[new_key] = new_value
print(my_dict)

my_dict ={"a":4,"b":4,"c":4}

num_unique_value = len(set(my_dict.values()))

if num_unique_value == 0:
    print("EMPTY")
elif num_unique_value == 1:
    print(True)
else:
    print(False)


string = "hello, world"
freq_dict = {}
for char in string.lower():
    if char.isalpha():
        if char in freq_dict:
            freq_dict[char]+=1
        else:
            freq_dict[char] = 1
print(freq_dict)

my_dict = {
    "a": [4,3,2],
    "b": [5,3,7],
    "c": [1,9,10],
    "d": [3,4,1]
}
for list_value in my_dict.values():
    list_value.sort()

print(my_dict)

def find_max_value(lst):
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value
number = [3,7,2,9,5]
print(find_max_value(number))


#define function with argument or without argument

def add():
    x=20
    y=30
    c=x+y
    return c
sum = add()
print(sum)


def add(y):
    x=10
    c=x+y
    d=y-x
    return c,d,


def disp():
    def show():
        return "show function:"
    result = show() + "display function"
    return result
print(disp())

def disp(st):
    def show():
        return "show function"
    result = show() + st + "disp function"
    return result
print(disp("geekyshow"))

def show(name,age):
    print(f"name:{name} age:{age}")
show(age = 62, name = "geekyshow")

def show(name,age=20):
    print(f"name : {name} age : {age}")
show(name = "geekyshows")

def add(*num):
    z=num[0]+num[1]+num[2]
    print("addition:",z,num[3])
add(5,2,4,"zing")

def add(x ,*num):
    z= x + num[0] + num[1]
    print("addition:",z)
add(5,2,4)

def add(x,y,**num):
    z=x + num["a"]+num["b"]
    print("addition:",z)
add(3,6,a=5,b=6)

a=50
def show():
    x=10
    print(x)
    print(a)
show()

def numbers(n):
    if n <= 20:
        print(n)
        numbers(n + 1)
numbers(1)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
result = factorial(5)
print(result)

