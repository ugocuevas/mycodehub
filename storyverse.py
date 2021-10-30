#In this code, the story never changes, but the characters do
husbandName = input("Please enter the husband's name: ")
wifeName = input("Please enter the wife's name: ")
sisterName = input("Please enter the sister's name: ")
dadName = input("Please enter the dad's name: ")
mumName = input("Please enter the mum's name: ")
cityName = input("Please enter the name of the city: ")

print(f'\n \033[1m{husbandName}\033[0m and \033[1m{wifeName}\033[0m are planning to pay a surprise visit to {husbandName}\'s parents, \033[1m{dadName}\033[0m and \033[1m{mumName}\033[0m in \033[1m{cityName}\033[0m')
print("They have been planning this trip for two months with " + husbandName + "'s sister, " + "\033[1m" + sisterName +  ". \033[0m")
print(f'However, for the past three days, {sisterName}\'s phone has not been reachable. \nOn the Dday, as {husbandName} and {wifeName} are preparing to drive out of their garage, a black SUV skids to a stop across the exit of their garage')
print("Suddenly, the door of the SUV opens and " + dadName + ", " + mumName + " and " + sisterName + " come down from the vehicle.")
print(f' \n {dadName}, {mumName} and {sisterName}: Surprise!!! \n')
