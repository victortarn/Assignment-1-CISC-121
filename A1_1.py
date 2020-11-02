x = 0

# While loop keeps program running untill it is exited
while x == 0:
    name = input('Enter a first name: ')

    # Checks if there are any numbers in input
    def hasDigits(name):
        return any(char.isdigit() for char in name)
    

   # checks if there are any numbers or if input is null 
    if  hasDigits(name) or name == '':
        print ('Please try again and enter your name.')
    else:
        name = name.upper()
        print ('Your Name in all capital letters is %s.' % name)
        
    restart = input('Type anything to enter name or "exit" to exit: ')

    #Ends program when exit is typed
    if restart == 'exit':
        exit()
    
