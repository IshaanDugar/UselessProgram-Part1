# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 12:55:35 2020

@author: Ishaan
"""

#IMPORTING ALL REQUIRED LIBRARIES
from random import randint
from collections import Counter
from matplotlib import pyplot as plt
import requests
import bs4
import re
import numpy as np

output = []         #Creating a list for the output


x = 0


outputstr = ''      #To print the output in string from list



def forH(lis):                  #A function for letter 'H'

    '''
A for loop that generates 100 numbers and checks for a number and then appends the letter
    '''

    for i in range(100):
        if i == 72:
            lis.append('H')



def forE(val, lis):             #A function for letter 'E'

    '''
A while loop that keeps increasing until it meets its satisfaction to append the letter
    '''
    while val != 99:
        val += 1
        if val == 99:
            lis.append('e')
            break



def for1L(lis):                 #A function for letter 'L'
    '''
A while loop that checks for the length of a list that gets  with random lengths until it meets it requirements
    '''               
    randomrange = 0
    templis = []
    seclis = []

    while len(templis) < 100:
        randomrange = randint(0, 200)
        templis = list(i for i in range(randomrange))

        if len(templis) >= 100:
            break
    
    if 144 in templis:
        lis.append('l')


        
def for2L(lis):                 #A function for letter 'L'
    '''
A while loop that keeps generating random numbers until they both are equal to another number and then appending a letter
    '''
    x1 = 0

    y1 = 0

    while True:
        x1 = randint(0, 1000)

        y1 = randint(0, 1000)
        
        if x1 == y1 == 777:
            lis.append('l')
            break


            

def forO(lis):                  #A function for letter 'O'
    '''
An integer here appears 'n' times until the index of the string meets 'O' and then appends it
    '''

    randomList = [1,2,34,2,5,639,7,323,9,4,7,47,5,6,32,21,5,7,8,2,7,346]

    letterO = 'Hello'

    count = randomList.count(7)

    lis.append(letterO[count])




def forSpace(lis):              #A function for a Space Between Hello and world
    '''
Plotting a sine graph and then checks if a value of sine meets in the x-axis and appends a space
    '''

    time = np.arange(0, 10, 0.1)
    
    amplitude = np.sin(time)

    plt.plot(time, amplitude)

    plt.grid(True, which='both')

    plt.axhline(y=0, color='k')

    if 0.5 in time:

        lis.append(' ')



def forW(lis):                  #A function for letter 'W'
    '''
Using regular expressions to find digits in the string that are the index position of the alphabets
    '''

    letters = 'I\'m typing some useless stuff containing the 23rd letter of the alphabets.'

    pattern = r'\d\d'

    loc = re.search(pattern, letters)

    alphas = 'abcderfghijklmnopqrstuvwxyz'

    pos = loc.group()

    lis.append(alphas[int(pos)].upper())



def for2O(lis):                  #A function for letter 'O'
    '''
Checking the intersection of the 2 lists and sorts it and arranges it and the the index of the letter is generated
    '''

    lis1 = [1, 3, 5, 6, 8, 8, 9]
    lis2 = [123,54,6,578,4,54,51,235,2538]
    
    intset = set.intersection(set(lis1), set(lis2))

    intlis = list(intset)

    randstr = 'HHHHEEEEEELLLLLLOOOOOO' 

    arranged = list(set(randstr))

    order = sorted(arranged)

    lis.append(order[intlis[0] - 3].lower())



def forR(lis):                    #A function for letter 'R'
    '''
Obtaining the title of a website called 'code.org' and appending a letter from the title

In case some connection error arises, it stops the whole program
    '''

    try:
        link = requests.get('https://code.org')

        style = bs4.BeautifulSoup(link.text, "lxml")

        title = style.select("title")

        titletotxt = title[0].getText()

        lis.append(titletotxt[3])


    except:
        print("\n\nNO ACTIVE CONNECTIONS! PLEASE CONNECT TO A NETWORK CONNECTION\n\n")



def for3L(lis):                     #A function for letter 'L'
    '''
Creating a class and defining a function to join a letter into the output
    '''
    class LetterL:
        def __init__(self, letter, lis):
            self.letter = letter
            self.lis = lis

        def insert():
            lis.append('l')


    aClassAttribute = LetterL.insert()

    
def forD(lis):                      #A function for letter 'D'
    '''
Opening a file and inserting a letter from that file into our output list
If you do not have the 'LetterD.txt' on your device, it creates it and you will have to run it again!
    '''

    try:
        f = open("LetterD.txt", 'r')
        text = f.read()
        count = 0

        while count != 15:
            count += 1

            if count == 15:
                lis.append(text[count].lower())
                break

    except FileNotFoundError:
        print('\n\nFile was not found. It has been created.RETRY AGAIN!\n\n')

        f = open("LetterD.txt", 'w+')
        f.write('This is letter D')





#Calling the functions and inserting the letters into the output list

forH(output)
if 'H' in output:
    forE(x, output)
    if 'e' in output:
            for1L(output)
            if 'l' in output:
                for2L(output)
                if 'l' in output:
                    forO(output)
                    if 'o' in output:
                        forSpace(output)
                        if ' ' in output:
                            forW(output)
                            if 'W' in output:
                                for2O(output)
                                if 'o' in output:
                                    forR(output)
                                    if 'r' in output:
                                        for3L(output)
                                        if 'l' in output:
                                            forD(output)


#For loop to convert the letters in the list to String
for i in output:
    outputstr += i

#Printing the String
if 'Hello World' in outputstr:
    print(outputstr)

else:
    print("  ")