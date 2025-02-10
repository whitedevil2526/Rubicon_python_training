#day 4
#set 

# Duplicates are avoided
b = {10, 20, 'GeekyShows', 'Raj', 40, 10, 10}
print(b)
print()

list1 = [9,8,4,1]
x = set(list1)
y = list(x)
y.reverse()
print(y)


# Set Methods
a = {'Rahul', 'Raj', 'Sonam', 'Rani'}
b = {'Sumit', 'Rahul', 'Rani', 'Python', 'Java'}

print("A:",a)
print("B:",b)
print()

# intersection() Method
# returns item which exists in both sets
ism = a.intersection(b)
print("Intersection:", ism)
print()

# union() Method
# Returns all item from original set and all items from specified set
um = a.union(b)
print("Union:", um)
print()

# difference() Method
# Returns items that exist only in first set, and not in both sets
dm = a.difference(b)
print("Difference:", dm)
print()

# issubset() Method
#Returns True if all items in the set exists in the specified set
isub = a.issubset(b)
print("issubset:", isub)
print()

# issuperset() Method
# Returns True if all items in the specified set exists in the original set
isup = a.issuperset(b)
print("issuperset:", isup)
print()

# Sets - clear() Method
a = {10, 20, 'GeekyShows'}
print("Before Clear",a)
print(id(a))
print()
a.clear()
print("After Clear",a)
print(id(a))

my_list=['abhijeet','sushil','aakash']
new_list=[]
for name in my_list:
    name=name + "hii"
    new_list.append(name)
print(new_list)

new_list = [name + "hii" for name in my_list]
print(new_list)


my_list = ['abhijeet', 'sushil', 'aakash']
surname = 'kumar'
new_list = []
for name in my_list:
    full_name = f"{name} {surname}"
    new_list.append(full_name)
print(new_list)
new_list = [f"{name} {surname}" for name in my_list]
print(new_list)

# Dictionary Comprehension
lst = [(101, "Rahul"), (102, "Raj")]
dict1 = {k:v for k,v in lst}
print(dict1)


# Without Dict Comprehension
dict1 = {}
for n in range(10):
	dict1[n]=n**2
print(dict1)

# With DIct Comprehension
dict2 = {n:n**2 for n in range(10)}
print(dict2)


# Without Dict Comprehension (Conditional)
dict1 = {}
for n in range(10):
	if n%2==0 :
		dict1[n]=n*2
print(dict1)

# With Dictionary Comprehension (Conditional)
dict2 = {n:n*2 for n in range(10) if n%2==0}
print(dict2)


# Without Dict Comprehension (Nested Conditional)
dict1 = {}
for n in range(10):
	if n%2==0 :
		if n%3==0:
			dict1[n]=n*2
print(dict1)

# With Dictionary Comprehension (Nested Conditional)
dict2 = {n:n*2 for n in range(10) if n%2==0 if n%3==0}
print(dict2)


# Without Dict Comprehension (If Else)
dict1 = {}
for n in range(10):
	if n%2==0 :
		dict1[n]=n
	else:
		dict1[n]="Invalid"
print(dict1)

# With Dictionary Comprehension (If Else)
dict2 = {n:(n if n%2==0 else "Invalid") for n in range(10)}
print(dict2)

#list comprehension
list1 = [5, 3, 2, 5, 3, 4, 7]
list2 = [2, 5, 7,2]
merged_list = list1.copy()
for item in list2:
    merged_list.append(item)
print(merged_list)
item_counts = {item: merged_list.count(item) for item in merged_list}
print(item_counts)

item_counts = {item: (merged_list.count(item) if merged_list.count(item) % 2 == 0 else "Invalid") for item in merged_list}
print(item_counts)


# Initial lists of names
list1 = ["Alice", "Bob", "Charlie", "Alice", "Bob", "David", "Eve"]
list2 = ["Charlie", "Alice", "Eve", "Charlie"]
merged_list = list1.copy()
for name in list2:
    merged_list.append(name)
print("Merged List:", merged_list)
name_counts = {name: merged_list.count(name) for name in merged_list}
print("Name Counts:", name_counts)
name_counts = {name: (merged_list.count(name) if merged_list.count(name) % 2 == 0 else "Invalid") for name in merged_list}
print("Updated Name Counts:", name_counts)

#object is a blueprint of class 
#constructor assign the value by using "__"
class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.name}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2021)
car3 = Car("Rolls Royce", "Ghost", 2025)

car1.display_info()
print()
car2.display_info()
print()
car3.display_info()
print()

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def display_info(self):
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Area: {self.calculate_area()}")

rectangle1 = Rectangle(5, 3)
rectangle1.display_info()

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius

    def display_info(self):
        print(f"Radius: {self.radius}")
        print(f"Area: {self.calculate_area()}")

circle1 = Circle(4)
circle1.display_info()


class Employee:
    def __init__(self, name, salary, bonus=500):
        self.name = name
        self._salary = salary
        self.__bonus = bonus

    def display_details(self):
        return f"Name: {self.name}, Salary: {self._salary}"

    def get_bonus(self):
        return self.__bonus

emp = Employee("Alice", 50000)
print(emp.display_details())
print(emp._salary)
print(emp.get_bonus())

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_acnt(self, acnt_num, initial_bal):
        if acnt_num not in self.accounts:
            self.accounts[acnt_num] = initial_bal
            print(f"Account {acnt_num} created with initial balance: {initial_bal}")
        else:
            print(f"Account {acnt_num} already exists...")

    def deposit(self):
        acnt_num = input("Enter account number to deposit into: ")
        amount = float(input("Enter amount to deposit: "))
        if acnt_num in self.accounts:
            self.accounts[acnt_num] += amount
            print(f"Deposited {amount} into account {acnt_num}")
            print(self.accounts)
        else:
            print(f"Account {acnt_num} does not exist...")

    def withdraw(self, acnt_num, amount):
        if acnt_num in self.accounts:
            self.accounts[acnt_num] -= amount
            print(f"Withdrawn {amount} from account {acnt_num}")
            print(self.accounts)
        else:
            print(f"Account {acnt_num} does not exist...")
    def display_balance(self, acnt_num):
        if acnt_num in self.accounts:
            print(f"Balance for account {acnt_num}: {self.accounts[acnt_num]}")
        else:
            print(f"Account {acnt_num} does not exist...")

bank = Bank()
bank.add_acnt('123456789', 1000000)
bank.deposit()
bank.withdraw('123456789', 20000)
bank.withdraw('123456789', 20000)
bank.display_balance('123456789')

class HotelBillManager:
    def __init__(self):
        self.hotel_bills = {}

    def add_hotel_bill(self):
        bill_id = input("Enter bill ID: ")
        amount = float(input("Enter bill amount: "))
        gst_rate = float(input("Enter GST rate: "))
        if bill_id not in self.hotel_bills:
            gst_amount = amount * gst_rate / 100
            total_amount = amount + gst_amount
            self.hotel_bills[bill_id] = {
                'amount': amount,
                'gst_rate': gst_rate,
                'gst_amount': gst_amount,
                'total_amount': total_amount
            }
            print(f"Hotel bill {bill_id} added with amount: {amount}, GST: {gst_amount}, Total: {total_amount}")
        else:
            print(f"Hotel bill {bill_id} already exists...")

    def split_bill(self):
        bill_id = input("Enter bill ID to split: ")
        num_people = int(input("Enter the number of people: "))
        if bill_id in self.hotel_bills:
            total_amount = self.hotel_bills[bill_id]['total_amount']
            split_amount = total_amount / num_people
            print(f"Hotel bill {bill_id} split among {num_people} people: {split_amount} each")
        else:
            print(f"Hotel bill {bill_id} does not exist...")

hotel_manager = HotelBillManager()
hotel_manager.add_hotel_bill()
hotel_manager.split_bill()
