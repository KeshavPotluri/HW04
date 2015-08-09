#!/usr/bin/env python
# HW04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports

import random

# Body

def guessingGame():

	# Generate a random number
	randNum = random.randint(1,25)
	
	# Starts a count to give the user a max of 5 chances
	count = 0

	# Prompt the user as long as the number of guesses have been less than 5
	while count < 5 :
		try:
			# Get the user input and convert it to int
			guess = raw_input("The number is between 1 - 25. Guess the number: ") 
			guess_int = int(guess)
		except:
			# If the entered number is not an int, throw a validation
			print "Please enter a number!!"
		else:
			# If the user enters the correct number, end the game with success message
			if guess_int == randNum:
				print "You have guessed the correct number!!"
				break
			else:
				# Increment a count and tell the user if the guess is too high or too low
				count = count + 1
				if guess_int> 25 or guess_int<0:
					print "Please select a number between 1 and 25!!! Try again!! You have " + str(5 - count) + " chances remaining."
				elif guess_int > randNum:
					print "Too High!!! Try again!! You have " + str(5 - count) + " chances remaining."
				else:
					print "Too Low!!! Try again!! You have " + str(5 - count) + " chances remaining."

	else:
		# If the user uses up all the 5 chances, end the game and show a message
		print "Oops!!! You are out of chances!!! Better Luck Next Time!!!"

################################################################################
def main():


    print("Hello World!") # Remove this and replace with your function calls
    guessingGame()
    

if __name__ == '__main__':
    main()