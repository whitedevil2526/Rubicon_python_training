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