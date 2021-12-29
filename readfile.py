#Simple file manipulation
#To open a file, we use open(filename, 'modifier'):

filename = 'practicetext.txt'
#One way of opening and closing files
# new_file = open(filename, 'r')

# new_file.close()

with open(filename, 'r') as f:   #r means read
    contents = f.read()
print(contents)
