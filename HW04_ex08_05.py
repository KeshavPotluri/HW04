#!/usr/bin/env python
# HW04_ex08_05

# The following program counts the number of times the letter a appears in a 
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print count

# Encapsulate this code in a function named "count", and generalize it so that 
# it accepts the string and the letter as arguments.

################################################################################
# Imports


# Body

def count(inputString, inputLetter):
	count = 0

	word = str(inputString)
	letter = str(inputLetter)

	if len(letter) != 1:
		print "Please enter a letter in the second argument."
	else:
		for char in word:
			if char == letter:
				count = count + 1
		print "The letter " + letter + " is repeated " + str(count) + " times in the word " + word +"."




################################################################################
def main():

    # Remove print("Hello World!") and add several functions calls to count()
    # below, passing various strings and letters
    # print("Hello World!") 

    count(1,2)
    count("Hello",2)
    count("Hello","l")
    count("Hello","ue")
    count(111111,1)
    

if __name__ == '__main__':
    main()