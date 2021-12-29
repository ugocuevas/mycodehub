#Simple file manipulation
#To open a file, we use open(filename, 'modifier'):

filename = 'Storytime.txt'
story = """\nChima and Tolu laughed at them.\n 
Then Chidi stood up and chased them away"""

with open(filename, 'a') as f:
    f.write(story)