# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    elif n <= 1:
        return 1

    return n * (factorial(n - 1))


# reverse



# bunny
def bunny(count):

    if count < 0:
        raise ValueError
    
    elif count == 0:
        return 0
    
    return 2 + bunny(count - 1)


# is_nested_parens


