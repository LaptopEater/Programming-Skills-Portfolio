
UserPassword = 12345
Password_Attempts = 5
Password_Limit = ""
outofguess = False

#I designed a password that would deny any user input that does not correlate with the passworrd variable 
#I coded a boolean method to deduct the ammount of attempts left and a if else statement to what would happen after.
while Password_Attempts != Password_Limit and not outofguess:
    if Password_Attempts > 0:
        passwordleft = Password_Attempts
        Password_Limit = input(f"Please Enter your password (Password Attempts Remaining) {Password_Attempts}:")
        Password_Attempts = Password_Attempts - 1
    else:
        outofguess = True
if outofguess:
    print("You have exceeded your max number of attempts, The Local Authorities have been Alerted.")
else:
    print("Welcome to the Website.")

    
    





"""
I want the system to make a loop to be able to loop the incorrect passwords until it is correct , or until the attempts run out
whilst also displaying messages if the password is correct or not.


"""
