# helping method for adding whitespaces before/after the given string. Used mainly for terminal text formatting
def make_name_same_length(name, length, end):
    num_of_spaces = length - len(str(name))
    if end:
        return str(name) + (num_of_spaces * " ")
    return (num_of_spaces * " ") + str(name)


# magic method that just works. If the thing is a digit, it returns it in an integer form.
def make_int(thing):
    if thing.isdigit():
        return int(thing)
    return thing
