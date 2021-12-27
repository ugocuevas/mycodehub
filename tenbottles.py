#Populating the ten green bottles song

def green_bottles(bottles):
    song = ''
    #Function to sing the green bottles song
    while bottles > 1:
        #First line
        first_line = f"{bottles} green bottles standing on the wall "
        line_one = f"{first_line}\n"
        line_two = "If one green bottle should accidentally fall down, we'll have \n"
        bottles -= 1
        #Second line
        second_line = f"{bottles} green bottles standing on the wall \n"
        if bottles == 1:
            line_three = f"One green bottle standing on the wall..."
        else:
            line_three = f"{second_line}"
        rhyme = line_one + line_two + line_three
        song += rhyme
    return song

# print(green_bottles(10))
        
file_name = 'ten_green_bottles.txt'
with open(file_name, 'w') as f:
    try:
        f.write(green_bottles(10))
    except:
        print("Something went wrong. Please recheck the code")