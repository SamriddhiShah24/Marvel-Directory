print('Number Guessing Game')
print('Enter a number between 1-10')


firstGuess=int(input('Enter your first guess'))


if firstGuess==6:
    print("Superb! You guessed the Number !!")
elif firstGuess<4:
    print("Too low, try a higher number...")
    secondGuess=int(input('Enter your second guess'))
elif firstGuess==5:
    print("Close... Keep trying")
    secondGuess=int(input('Enter your second guess'))

elif firstGuess>7:
    print("Too far, try a lower number")
    secondGuess=int(input('Enter your second guess'))


if  secondGuess==6:
    print("Superb! You guessed the Number !!")
elif secondGuess<4:
    print("Try Again Later, the number is 6")
    
elif secondGuess==5:
    print("Try Again Later, the number is 6")
    
elif secondGuess>7:
    print("Try Again Later, the number is 6")
    secondGuess=int(input('Enter your first guess'))
