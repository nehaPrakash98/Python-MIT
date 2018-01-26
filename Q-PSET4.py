# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 18:10:14 2018

@author: Neha
"""
import hint_word
import random
dict = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

inFile = open("words.txt", 'r')
wordList = []
for line in inFile:
    wordList.append(line.strip().lower())
flag = True
while flag: 
    print("Welcome to the game of scrabble!")
    n = len(wordList)
    print(n, end='')
    print(" words loaded")
          
    def createHand():
        diff = input("Pick your difficulty, type high/low: ")
        n=0
        while n==0:
            if diff == 'high':
                n = random.randint(5, 7)
                break
            elif diff == 'low':
                n = random.randint(7, 13)
                break
            else:
                print("Please type a valid difficulty level!")
            diff = input("Pick your difficulty, type high/low: ")
            
        nv = n//3
        cv = n-nv
        hand = {}
        for i in range(nv):
            l = VOWELS[random.randint(0, len(VOWELS)-1)]
            hand[l] = hand.get(l, 0)+1
        for i in range(cv):
            l = CONSONANTS[random.randint(0, len(CONSONANTS)-1)]
            hand[l] = hand.get(l, 0)+1
            #hand.get(l, 0)
        return hand
    
    def getScore(word, n):
        c = 0
        for letter in word:
            c += dict[letter]
        c = c*len(word)
        if len(word) == n:
            print("Congradulations! Your word uses all letters in the hand. You get a bonus 50!")
            c = c+50
        return c
        c = 0
        
    def isValid(word, hand): 
        h1 = hand.copy()
        c=0
        for letter in word:
            if letter in h1.keys():
                c+=1
                if h1[letter]>0:
                    h1[letter]-=1
                else:
                    return False
                
        if word in wordList and c==len(word):
            return True
        else:
            return False
        
    def update(word, hand):
        h1 = hand.copy()
        for letter in word:
                h1[letter]-=1
        return h1
        
    def lenHand(hand):
        c = 0
        for key in hand.keys():
            if hand[key]>0:
                c+=hand[key]
        return c
    
    score = 0
    total = 0              
    count = 0
    
    hand = createHand()
    length_of_hand = lenHand(hand) 
    hand1 = hand.copy()
    
    print("Current hand is: ", end='')
    print(hand)
    s1 = input("To change the hand, press 1 or press any other key to continue")
    
    while s1=='1':
        hand = createHand()
        hand1 = hand.copy()
        print("Current hand is: ", end='')
        print(hand)
        s1 = input("To change the hand, press 1 or press any other key to continue: ")
    
    
    s = input("Enter a word or \".\" to quit or '?' for a hint: ")
    while s!='.':   
        if s == '?' and lenHand(hand)>=3:
            if count==0:
                ls = hint_word.hint(hand)
                print("You have exhausted your one hint!")
                print(ls)
                count = 1
                
            else:
                print("No more hints for you!")
                
        elif s == 'u':
            hand = hand1.copy()
            count = 0
            
        elif(isValid(s, hand)):
            score = getScore(s, length_of_hand)
            print("Potential score for the word \' "+str(s)+" \' is "+str(score)+" points.")
            pot_score = input("Do you want to retry? y/n: ")
    #        print(pot_score)
            while pot_score!='':
                if pot_score == 'n':
                    print("Congradulations! You earned "+str(score)+" points")
                    total += score
                    print("Total Score: "+str(total)+" points.")
                    hand = update(s, hand)
                    pot_score = ''
                elif pot_score == 'y':
                    pot_score = ''
                    continue
                else:
                    print("Enter either \'y\' ot \'n\'!")
                    pot_score = input("Do you want to try another word to increase your score? y/n: ")
            if lenHand(hand)<2:
                break
        else:
            print("Invalid word! Please try again!")
            
        print("Current hand: ", end='')
        print(hand)
        s = input("Enter a word or \".\" to quit or '?' for a hint or press 'u' to undo: ")
        
            
    if s==".":
        print("Quitter!")
        print("Total Score: "+str(total)+" points.")
    elif lenHand(hand)<2:
        print(hand)
        print("Game over. You ran out of letters!")
        print("You won! Total score: "+str(total)+" points.")
            
    f = open("high_score.txt", "a+")
    f.write(str(total)+"\n")
    high_s = []
    f.seek(0)
    
    for line in open('high_score.txt'):
        num = int(line.rstrip())
        high_s.append(num)
    f.close()
    
    high_s.sort(reverse=True)
#    print(high_s)
    print("\n   High Scores")
    for i in range(5):
        print("\t"+str(high_s[i]), end='')
        if total == high_s[i]:
            print("  YOU")
            print("\n")
        else:
            print("\n")
        
    play_again = input("Press 1 to play again or and other letter to quit: ")
    if play_again == '1':
        flag = True
    else:
        flag = False
    


    
        




            
        
        
    
