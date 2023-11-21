# Task

# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.

# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false


# First solution
# Time 4.06ms on codewars
def is_isogram1(string):
    low = string.lower()
    set_string = set(low)
    if len(set_string) == len(low):
        return True
    else:
        return False


# Solution after revision
# Time 3.84ms on codewars
def is_isogram2(string):
    return True if len(string.lower()) == len(set(string.lower())) else False


# Due to the finalization of the solution, the execution time of the program decreased


# Best practices
# Time 3.69ms on codewars
def is_isogram3(string):
    return len(string) == len(set(string.lower()))


print(is_isogram1('abA'))
print(is_isogram2('abA'))
print(is_isogram3('abA'))
