calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    a_len = len(string)
    str_upper = string.upper()
    str_lower = string.lower()
    b_tuple = (a_len, str_upper, str_lower)
    return (b_tuple)


def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()

    if string_lower in (elem.lower() for elem in list_to_search):
        return "True"
    else:
        return "False"


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

print(calls)
