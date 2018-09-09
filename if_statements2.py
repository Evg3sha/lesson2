def strings_compare(string1, string2):
    if not isinstance(string1, str) or not isinstance(string2, str):
        return 0
    if string1 == string2:
        return 1
    if string1 != string2 and string2 == 'learn':
        return 3
    if string1 != string2 and len(string1) > len(string2):
        return 2


print(strings_compare(1, 2), strings_compare(' ', 2), strings_compare(1, 'test_strings'))
print(strings_compare('test_strings', 'test_strings'))
print(strings_compare('test_strings_len', 'test_strings'))
print(strings_compare('test_strings', 'learn'))
