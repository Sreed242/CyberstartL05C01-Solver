input_table2 = input("Enter the numbers in table 2   ")
table2 = input_table2.split()
input_table1 = input("Enter the numbers in table 1   ")
table1 = input_table1.split()
for num in range(len(table2)):
    table2[num] = int(table2[num])
for num in range(len(table1)):
    table1[num] = int(table1[num]) 
difference = []
for num2, num1 in zip(table2,table1):
    difference.append(num2 - num1)
total = sum(difference)
print(total)
