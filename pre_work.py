# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello_" + user_name +"!")

hello_name("USERNAME")

# Question 2 
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for odds in range(1,100,2):
        print(odds)
first_odds()

# Question 3 
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    max_num = a_list[0]
    for i in a_list:
        if i > max_num:
            max_num = i
    return max_num

print(max_num_in_list([300,400,600,-1,12]))

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
 
def is_leap_year(a_year):
    leap_year = False
    if a_year % 4 == 0:
        leap_year=True
    if a_year% 100 == 0:
        leap_year = False
    if a_year % 400== 0:
        leap_year = True
    return leap_year
    
print(is_leap_year(2400))

# Question 5 
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def  is_consecutive_list(a_list):
    list = sorted(a_list)
    print(list)
    for i in range(len(list)):
        if list[i] == (list[i+1]):
            return False
        else:
            return True
    
        
print(is_consecutive_list([2,3,4,5,6,7]))


