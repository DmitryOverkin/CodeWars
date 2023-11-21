# Task

# Complete the function that takes a non-negative integer n as input,
# and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).

def powers_of_two(n):
    powers = []
    for i in range(0, n + 1):
        lst = 2 ** i
        powers.append(lst)  # my solution of this problem
    return powers


print(powers_of_two(4))


def powers_of_two_2(n):
    return [2 ** x for x in range(n + 1)]  # Perfect solution


print(powers_of_two_2(4))
