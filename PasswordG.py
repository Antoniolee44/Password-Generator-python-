import string 
import random 

#getting a Password Length 
length = int(input('Enter password Length: '))

print('''Choose character set for password frome these 
1.Digits 
2.Letters 
3.Special characters 
4.Exit''') 

characterList = ""

#getting character set for password
while(True): 
    choice = int(input('pick a number'))
    if(choice == 1): 
        #adding letters to psssible characters
        characterList += string.ascii_letters
    elif(choice == 2):
        #adding digits to the password
        characterList += string.digits
    elif(choice == 3): 
        #adding special Characters 
        characterList += string.punctuation
    elif(choice == 4): 
        break 
    else:
        print('please pick a valid option')
password = []

for i in range(length):
    
    randomchar = random.choice(characterList)
    password.append(randomchar)

print("the random password is " + "".join(password))