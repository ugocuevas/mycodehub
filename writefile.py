#Simple file manipulation
#To open a file, we use open(filename, 'modifier'):

filename = 'Storytime.txt'
story = """Chidi and Vee went to the sea a pail of water.\n 
Chidi fell down and broke his crown and Vee came tumbling after"""

with open(filename, 'w') as f:
    f.write(story)
    
#Write Ten green bottles standing on the wall (up till one green bottle) to an empty file
#Read one verse of Twinkle twinkle little star and print it on python