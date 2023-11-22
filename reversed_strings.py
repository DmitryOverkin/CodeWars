# Task

# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

# First solution
# time 651ms
def solution(string):
    return string[::-1]


# Second solution
# Time 481ms 
def reverse_str(string):
    lst = list(string)
    str = ''
    for i in range(len(lst)):
        str += lst[-1]
        lst.pop(-1)
    return str


print(solution(('world')))
print(reverse_str('hello'))
