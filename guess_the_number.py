from random import randint

print("These are the following instructions")
print("Whenever your want to exit the game type 'EXIT' whenevet asked to guess the number !")
print("Enjoy !")

print("Enter your range : ")
min = int(input("Enter min value of range : "))
max = int(input("Enter max value of range : "))
randomNumber = randint(min, max)
print("Number generated successfully")
guessedNumber = input("Guess the number : ")

try :
    while(int(guessedNumber) != randomNumber) :
        if(randomNumber-int(guessedNumber) in range(-2,2)) :
            print("So Close !")
            guessedNumber = input("Try Again :")
        elif(randomNumber-int(guessedNumber) in range(-5,5)) :
            print("Too far !")
            guessedNumber = input("Try Again :")
except ValueError :
    if(guessedNumber == "EXIT") :
        print("Enjoy your day !")
        exit()
    else :
        print("Something went wrong")
        guessedNumber = input("Try Again :")

print("Congrats, You guessed it !")