string1 = input('enter a string: ')
char_list = []
'''
#to_list = list(string1)
#print(to_list)

split_str = string1.split(' ')
print(split_str)
a, b, c = split_str

char_count = {}
for char in a:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)
'''
input_string = input('enter a string')
string_to_list = []
for char in input_string:
    string_to_list.append(char)
print(string_to_list)

string_to_list = list(input_string)