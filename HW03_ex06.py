#!/usr/bin/env python
# HW03_ex06
# (1) Please comment your code.
# (2) Please be thoughtful when naming your variables.
# (3) Please remove development code before submitting.
################################################################################
# Exercise 1
# When you submit only include your final function: compare
from __builtin__ import raw_input

def compare(x,y):
    if (x>y):
        return 1
    elif(x==y):
        return 0
    else:
        return -1






################################################################################
# Exercise 2
# When you submit only include your final function: hypotenuse
# Do develop incrementally. Do not share here.

def hypotenuse(x,y):
    import math
    print "\nfirst side = ",x
    print "second side = ", y
    xsq = x**2
    ysq = y**2
    print 'first side square = ', xsq
    print 'second side square = ', ysq
    z = xsq + ysq
    print "sum = ",z
    result = math.sqrt(z)
    return result
    





################################################################################
# Exercise 3
# When you submit only include your final function: is_between

def is_between(x, y, z):
    if (x <= y <= z):
        return True
    else:
        return False






################################################################################
# Exercise 6
# When you submit only include your final function: is_palindrome
def is_palindrome(word):
    length = len(word)
    def first(word):
        return word[0]
    def last(word):
        return word[-1]
    def middle(word):
        return word[1:-1]
        
    def check(word):
        if ((length%2) == 0):
            x = first(word)
            y = last(word)
            if (x == y):
                z = middle(word)
                if (len(z) == 0):
                    print "It is a palindrome"
                    return
                check(z)
            else:
                print "It is not a palindrome"
        else:
            if ((length%2) != 0):
                x = first(word)
                y = last(word)
                if (x == y):
                    z = middle(word)
                    if (len(z) == 1):
                        print  "It is a palindrome"
                        return
                    check(z)
                else:
                    print "It is not a palindrome"
                    
    check(word)
            
        
    
################################################################################
# Exercise 7
# When you submit only include your final function: is_power

def is_power(a,b):
    if ((a%b == 0) and ((a/b)%b) == 0):
        return True
    else:
        return False
    
    

################################################################################
def main():
    """Your functions will be called within this function."""
    ############################################################################
    # Use this space temporarily to call functions in development:
    print("Hello World!")


    ############################################################################
    # Uncomment the below to test and before commiting:
    print "Exercise 1"
    print"------------------"
    print compare(1,1)
    print compare(1,2)
    print compare(2,1)
    #Exercise 2
    print "\nExercise 2"
    print"------------------"
    print ('hypotenus =' , hypotenuse(1,1))
    print ('hypotenus =' , hypotenuse(3,4))
    print ('hypotenus =' , hypotenuse(1.2,12))
    # # Exercise 3
    print "\nExercise 3"
    print"------------------"
    print is_between(1,2,3)
    print is_between(2,1,3)
    print is_between(3,1,2)
    print is_between(1,1,2)
    
    # # Exercise 6
    print "\nExercise 6"
    print"------------------"
    is_palindrome("Python")
    is_palindrome("evitative")
    is_palindrome("sememes")
    is_palindrome("oooooooooooo")
    
    # # Exercise 7
    print "\nExercise 7"
    print"------------------"
    print is_power(28,3)
    print is_power(27,3)
    print is_power(248832,12)
    print is_power(248844,12)


if __name__ == "__main__":
    main()