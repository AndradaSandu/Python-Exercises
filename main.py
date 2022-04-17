
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in
# a comma-separated sequence on a single line.

# lst = []
# for i in range(2000,3200):
#     if(i % 7 == 0 and i % 5 != 0):
#         lst.append(str(i))
# print(','.join(lst))

# Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied
# to the program: 8 Then, the output should be:40320

# x = int(input("Enter the factorial:"))
# fact = 1
# for i in range(1, x+1):
#     print('i', i)
#     fact = fact * i
#     print(fact)

# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.Suppose the following input is supplied to the program.


# x = int(input("Enter the range:"))
#
# dict = 1
#
# for i in range(1, x+1):
#     # print("i",i)
#     dict = i*i
#     print(i, ":", dict)

# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program : 34,67,55,33,12,98.

# input_string = input("Enter a list element separated by space ")
# list  = input_string.split()
# tuple = tuple(list)
# print("List:", list,'\n' "Tuple:", tuple)

# Define a class which has at least two methods:
#
# getString: to get a string from console input.
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
#
# Hints:
# Use init method to construct some parameters.
#
# class twoMethods:
#     def init(self, x):
#         self.x = x
#     def getString(self):
#         self.x = str(input("get a string: "))
#
#     def printString(self):
#         print(self.x.upper())
#
# obj = twoMethods()
# obj.getString()
# obj.printString()


# Write a program that calculates and prints the value according to the given formula:
#
# Q = Square root of [(2 _ C _ D)/H]
#
# Following are the fixed values of C and H:
#
# C is 50. H is 30.
#
# D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:
#
# 100,150,180


# _Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.*
#
# Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
#
# Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# x = int(input("Enter the row:"))
# y = int(input("Enter the column:"))
# lst = []
# for i in range(x):
#     a = []
#     print("i", i)
#     for j in range(y):
#         print("j", j)
#         a.append(i*j)
#     lst.append(a)
# print(lst)

# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

# a = 97
# b = 98
# c = 99
# d = 100
# e = 101
# f = 102
# g = 103
# h = 104
# i = 105
# j = 106
# k = 107
# l = 108
# m = 109
# n = 110
# o = 111
# p = 112
# q = 113
# r = 114
# s = 115
# t = 116
# u = 117
# v = 118
# w = 119
# x = 120
# y = 121
# z = 122


# input_string = input("Enter a list element separated by space ")
# words = input_string.split()
#
#
# for i in range(len(words)):
#     char = words[i]
#     print("char", char)
#     first_char_list = char[0]
#     print(first_char_list)
#
#     for j in range(len(words)):
#         char1 = words[j]
#         print("char1", char1)
#         first_char_list1 = char1[0]
#         if first_char_list.upper() < first_char_list1.upper():
#             aux = words[i]
#             words[i] = words[j]
#             words[j] = aux
# print(words)


# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# l = []
#
#
# while True:
#     word = input_string = input("Enter a word (Press q to quit) ")
#     if word == 'q':
#         break
#     else:
#         l.append(word.upper())
# print(l)


# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
#
# Suppose the following input is supplied to the program:
#
# hello world and practice makes perfect and hello world again
# Then, the output should be:
#
# again and hello makes perfect practice world

# input_string = input("Enter a list element separated by space ")
# words = input_string.split()
#
# if input_string != 0 :
#     input_string = sorted(list(set(words)))
#     print(input_string)


# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5
# are to be printed in a comma separated sequence.
#
# Example:
#
# 0100,0011,1010,1001
# Then the output should be:
#
# 1010


# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be
# printed in a comma-separated sequence on a single line.

# lst = []
#
# for i in range(1000,3000):
#     if i % 2 == 0:
#         lst.append(i)
# print(lst)

# Write a program that accepts a sentence and calculate the number of letters and digits.
#
# Suppose the following input is supplied to the program:
#
# hello world! 123
# Then, the output should be:
#
# LETTERS 10
# DIGITS 3

# x = input("Enter the sentence: ")
# counter = 0
# counter2 = 0
#
#
# for elem in x:
#     if ('a' <= elem <= 'z') or ('A' <= elem <= 'Z'):
#         counter += 1
#     else:
#         counter2 += 1
#
# print("letter are: ", counter)
# print("digits are: ", counter2)

# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#
# Suppose the following input is supplied to the program:
#
# Hello world!
# Then, the output should be:
#
# UPPER CASE 1
# LOWER CASE 9

# x = input("Enter the sentence: ")
# counter = 0
# counter2 = 0
#
# for el in x:
#     if ('a' <= el <= 'z'):
#         counter += 1
#     elif ('A' <= el <= 'Z'):
#         counter2 +=1
#
# print("UPPER CASE", counter)
# print("LOWER CASE ", counter2)

# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#
# Suppose the following input is supplied to the program:
#
# 9
# Then, the output should be:
# 11106

# y = input("enter the number: ")
# x = int(input("enter the range: "))
# total = 0
# temp = str()
#
# for i in range(x):
#     print("i", i)
#     temp += y
#     total += int(temp)
#     print(total)