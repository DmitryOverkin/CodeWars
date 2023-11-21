# Task
# Create a function that takes 2 integers in form of a string as an input,
# and outputs the sum (also as a string):


# my solution
def sum_str(a, b):
    if a == '':
        a = '0'
    if b == '':
        b = '0'
    return str(int(a) + int(b))


print(sum_str("", 2))
print(sum_str(34, 2))


# Perfect solution
def sum_str_2(a, b):
    return str(int(a or 0) + int(b or 0))


print(sum_str_2("", 2))
print(sum_str_2(34, 2))
