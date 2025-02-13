#add the data in txt file
file_path = "basic_file.txt"

file_content = []

with open(file_path) as file:
    for line in file:
        file_content.append(line)
print(file_content)

#update the data
data = "Hello,this is a sample text."

with open("basic_file.txt",'w') as file:
    file.write(data)

print("Data has been written to the file.")

#copy file from one txt to another txt file
with open("source.txt",'r') as source_file:
    with open("destination.txt",'w') as destination_file:
        for line in source_file:
            destination_file.write(line)
print("file copied successfully.")

#generate CSV file
import pandas as pd
df = pd.read_csv('example1.csv')
print(df)

#lambda function(annonumas function)

result = (lambda x,y : x+y)(10,15)
print(result)

#higher order
list_a = [1,2,3,4,5]
def square(x):
    return x**2
new_list = list(map(square,list_a))
print(new_list)

