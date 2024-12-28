filename = 'text.txt'

with open (filename) as file_object:
    lines = file_object.readlines()
    string = ''
    for line in lines:
        string += line.rstrip()

print(string)
print(len(string))        