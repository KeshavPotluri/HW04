# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 12 for guidance
# Please do provide function calls that test/demonstrate your function

import string


def rotate_letter(letter, n):
	if letter.isupper():
		start = ord('A')
	elif letter.islower():
		start = ord('a')
	else:
		return letter

	c = ord(letter) - start
	i = (c + n) % 26 + start
	return chr(i)


def rotate_word(word, n):
 	res = ''
	for letter in word:
		res += rotate_letter(letter, n)
	return res


def main():

    print rotate_word("cheer", 7)
    print rotate_word("melon", -10)
    

if __name__ == '__main__':
    main()