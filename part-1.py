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
def reverse(text):
    if len(text) <= 1:
        return text
    
    first_character = text[0]
    remaining = text[1:]

    return reverse(remaining) + first_character


# bunny
def bunny(count):

    if count < 0:
        raise ValueError
    
    elif count == 0:
        return 0
    
    return 2 + bunny(count - 1)


# is_nested_parens


