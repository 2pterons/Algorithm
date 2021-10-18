import re
import random
'''
p = re.compile("[a-zA-Z]+")
#m = p.match("python")
#m = p.match("3 python")
m = p.match("string goes here")
if m:
    print('Match found:', m.group())
else:
    print('No match')
print("#"*50)

m = p.search("python")
print(m)
print("#"*50)

result = p.findall("life is too short")
print(result)
print("#"*50)

result = p.finditer("life is too short")
print(result)
print("#"*50)
for r in result: print(r)
print("#"*50)

random.random()
random.randrange(1,51)
'''

#######################################################################
re = re.compile('[a-z]')

N = input()

a,b = map(str, input().split())
for i in range(1, 51):
    a.length - b.length
    if a[i] == b[i]:
        b.replace()

a = 'asdf'
b = 'dsfac'
find_b = b.find(b[-1])
result = b[:find_b]


my_string = 'Hello, what are doing?'
index = my_string.find(my_string[-1])
final_string = my_string[:index] + 'you ' + my_string[index:]
print(final_string)