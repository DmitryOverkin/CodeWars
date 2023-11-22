# Task

# Complete the function that takes two integers (a, b, where a < b) and
# return an array of all integers between the input parameters, including them.


# Firs solution
# Time: 490ms
def between(a, b):
    s = a
    lst = []
    lst.append(a)
    for i in range(a, b):
        if not s == b:
            s += 1
            lst.append(s)
    return lst


# Second solution
# Time: 479ms
def betwen2(a, b):
    return list(range(a, b + 1))


print(between(1, 7))
print(betwen2(1, 7))
