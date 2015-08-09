#!/usr/bin/env python
# HW04_ex08_11

# The following functions are all intended to check whether a string contains 
# any lowercase letters, but at least some of them are wrong. For each function, 
# describe what the function actually does (assuming that the parameter is a
# string).

# Do not merely paste the output as a counterexample into the documentation 
# string, explain what is wrong.

################################################################################
# Body

def any_lowercase1(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False
# The above function is wrong because it will only check whether the first char of 
# the string is lower case. For eg : any_lowercase1("Asd") will give a output as false
# while any_lowercase1("aSD") will return true.

def any_lowercase2(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
# The above function is wrong because it will always return True. It will check if 
# the character "c" is lower. Which is true always.

def any_lowercase3(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        flag = c.islower()
    return flag

# The above function is wrong because it will only check whether the last char of 
# the string is lower case. For eg : any_lowercase3("asD") will give a output as false
# while any_lowercase3("Asd") will return true.

def any_lowercase4(s):
    """Explain what is wrong, if anything, here.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
# The above function is correct.

def any_lowercase5(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        if not c.islower():
            return False
    return True

# The above function is incorrect because, as soon as the for loop encounters an
# upper case letter, it will return false which is incorrect For eg : 
# any_lowercase1("asD"). The function will check if all the letters in the word
# are lower case.

################################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong, 
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print any_lowercase1("Asd")
    print any_lowercase2("Asd")
    print any_lowercase3("AsD")
    print any_lowercase5("asD")
    

if __name__ == '__main__':
    main()