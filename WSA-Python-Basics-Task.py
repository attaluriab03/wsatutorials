# -*- coding: utf-8 -*-
### WSA TUTORIALS - PYTHON AND GITHUB BASICS TASK

### There are 12 problems to be completed.
### Do not worry about errors at first... They will all go away once you've attempted each problem
### INCLUDE ANY IMPORTS YOU NEED HERE, DO NOT PIP INSTALL ANY LIBRARIES
import math
import random


### Problem 1: Print out "hello". Python functions still need to return something so...
### Alternatively, you can return None after your print statement
def print_hello():
    return "Hello"



    
### Problem 2: Takes in two numbers (a and b) and returns their sum
def add(a, b):
    return a + b


    

### Problem 3: Takes in two numbers (a and b) and returns their difference
def sub(a, b):
    return a - b


    
    
### Problem 4: Takes in any two numbers (a and b) and returns their product
### CHALLENGE: use a for loop and your sum function to implement product
### HINT: think about what a for loop does and how sum relates to product
def product(a, b):
    return a * b
    
    
    
### Problem 5: Takes in any two numbers (a and b) and returns the quotient of a divided by b
### REQUIRED: only pass in numbers that are divisible
### CHALLENGE: use a while loop and your sub function to implement divide
### HINT: think about what a while loop does and how sub relates to division
def divide(a, b):
    return a / b
    
    
### Problem 6: Takes in a number (a) and returns the square of that number
### CHALLENGE: Use a combo of an if/else statement and a while loop
### HINT: think about edge (special) cases when certain numbers are squared
def square(a):
    return a * a
    
    
### Problem 7: given a string output what character occurs the most
### HINT: There are many ways to do this. One would be to store characters and the number of times they occur in a dictionary
### HINT: Another solution involves utilizing a for loop and re-setting the most popular character when the "new" most popular is found
### HINT: It will be helpful to use the .count() function. For more info, read https://www.programiz.com/python-programming/methods/string/count 
def max_char(word):
    wordIndex = 1;
    charCount = word.count(word[0])
    maxChar = ''
    while (wordIndex < len(word)):
        if (word.count(word[wordIndex]) > charCount):
            charCount = word.count(word[wordIndex])
            maxChar = word[wordIndex]
        wordIndex += 1 
    
    return maxChar
        
    
        
        
        
        
    
    
    
### Problem 8: given a list of numbers output a list of numbers greater than 10
def greater_than_ten(nums):
    newList = []
    for i in nums:
        if (i > 10):
            newList.append(i)
    return newList
        


### Problem 9: given a string with spaces return a list with each word seperated
### splitting points are designated by spaces in the string
### HINT: Use the .split() function
def split_string(word):
    return word.split()
    
    
### Problem 10: given a string and two character positions return a string with the characters between the two positions
### HINT: pos1 is inclusive while pos2 is the first character not included
### HINT: python strings start from index 0
def slice_string(string, pos1, pos2):
    return string[pos1:pos2]
    
    
    
### Problem 11: Return the sqrt of <num> only if <num> is a perfect square, otherwise return -1
### HINT: Use the Math Library (don't forget to import it)
def perfect_square(a):
    num = math.sqrt(a)
    if (num.is_integer()):
        return num
    else:
        return -1
            
    
        
    
    
### Problem 12: return a random number between the max and min parameters
### HINT: Use the random library (don't forget to import it)
def random_num_generator(min_num, max_num):
    return random.uniform(min_num, max_num)
    
    
def main():
    ### these are your test cases ###
    print_hello()
    print("Testing add:")
    print("EXPECTED: %d, ACTUAL: %d\n" % (5, add(2, 3)))
    print("Testing sub:")
    print("EXPECTED: %d, ACTUAL: %d\n" % (5, sub(7, 2)))
    print("Testing product:")
    print("EXPECTED: %d, ACTUAL: %d\n" % (10, product(2, 5)))
    print("Testing divide:")
    print("EXPECTED: %d, ACTUAL: %d\n" % (5, divide(10, 2)))
    print("Testing square:")
    print("EXPECTED: %d, ACTUAL: %d\n" % (25, square(5)))
    print("Testing max_char")
    print("EXPECTED: p ", "ACTUAL:", max_char("apple"), '\n')
    print("greater_than_ten")
    print("EXPECTED: [11, 14, 17, 22] ", "ACTUAL:", greater_than_ten([1,11,14,17,5,22]), '\n')
    print("Testing split_string")
    print("EXPECTED: ['Wolverine', 'Sports', 'Analytics'] ", "ACTUAL:", split_string("Wolverine Sports Analytics"), '\n')
    print("Testing slice_string")
    print("EXPECTED: ppl ", "ACTUAL:", slice_string("apple",1,4), '\n')
    print("Testing perfect_square")
    print("EXPECTED:", -1, "ACTUAL:", perfect_square(24))
    print("EXPECTED:", 5.0, "ACTUAL:", perfect_square(25), '\n')
    print("Testing random_num_generator")
    print("EXPECTED: number between 1 and 10 inclusive", "ACTUAL:", random_num_generator(1, 10))
    
    
if __name__ == "__main__":
    main()
    
    



