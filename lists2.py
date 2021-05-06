# 1. Sum the Numbers
# Create a list of numbers, print their sum.

list_of_numbers = [-40, 1, 2, 70, 33, 400]
print(list_of_numbers)

positive_numbers = []

multiple = 4
total = 0

# print('The total is %d' % sum(list_of_numbers))

for number in list_of_numbers:
    total = total + number
print('The total is now: ' + str(total))


# 2. Largest Numbers
# Create a list of numbers, print the largest of the numbers.

largest = list_of_numbers[0]
for num in list_of_numbers:
    if num > largest:
        largest = num
print('The largest number is: ' + str(largest))


# 3 Smallest Numbers
# Create a list of numbers, print the smallest of the numbers.
smallest = list_of_numbers[0]
for num in list_of_numbers:
    if num < smallest:
        smallest = num
print('The smallest number is: ' + str(smallest))

# 4 Even Numbers
for num in list_of_numbers:
    if num % 2 == 0:
        print('Even Number: %d' % num)

# 5 Positive Numbers I
for num in list_of_numbers:
    if num >= 0:
        print('Positive Number: %d' % num)

# 6 Positive Number II
for num in list_of_numbers:
    if num >= 0:
        positive_numbers.append(num)
print(positive_numbers)

# 7 Multiply a List
multiplied_numbers = [num * 2 for num in list_of_numbers]
print(multiplied_numbers)
