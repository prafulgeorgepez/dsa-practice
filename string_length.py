# normal method

s = input('enter a string: ')
count = 0

for char in s:
    count += 1
print(f'length of string is {count}')


# using recusion

s = input('enter a string: ')
def str_len(s):
    if s == "":
        return 0
    else:
        return 1 + str_len(s[1:])

l = str_len(s)
print(l)