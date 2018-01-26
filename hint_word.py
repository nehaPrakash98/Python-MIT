# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 19:51:06 2018

@author: Neha
"""
import random

dict = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'


inFile = open("words.txt", 'r')
wordList = []
for line in inFile:
    wordList.append(line.strip().lower())

#def createHand():
#    nv = 7//3
#    cv = 7-nv
#    hand = {}
#    for i in range(nv):
#        l = VOWELS[random.randint(0, len(VOWELS)-1)]
#        hand[l] = hand.get(l, 0)+1
#    for i in range(cv):
#        l = CONSONANTS[random.randint(0, len(CONSONANTS)-1)]
#        hand[l] = hand.get(l, 0)+1
#        #hand.get(l, 0)
#    return hand
#
#
def lenHand(hand):
    c = 0
    for key in hand.keys():
        if hand[key]>0:
            c+=hand[key]
    return c


def by_size(words, size):
    return [word for word in words if len(word) == size]   

def hint(hand):
    s = lenHand(hand)
    #print(s)
    words = by_size(wordList, 3)
    
    st = ''
    for key in hand.keys():
        if hand[key]>0:
            st += key
    #print(st)
    st = ''.join(sorted(st))
    
    
 #   print(words)
#    while words==[]:
#        s -= 1
#        words = by_size(wordList, s)
#    print(words)
#    ls = []
    
#    c = 0
 #names = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot']
# first_letters = ['A','B','C']
    output_names = [name for name in words if (name[0] in st)]
    output_names = [name for name in output_names if (name[1] in st)]
    output_names = [name for name in output_names if (name[2] in st)]
        
#        output_names = [name for name in output_names if (name[2] in st)]
    return output_names
    
            
#    wordlist = ['mississippi','miss','lake','que']

#    letters = set(st)
#    print(letters)
#    for word in words:
#        if letters & set(word):
#            print(word)
#            break
            
#    for word in words:
#        print("inFor")
#        if word in st:
#            print("in if")
#            print(word)
#            break
      
#    low = 20
#    for key in hand.keys():
#        if hand[key] < low:
#            low = hand[key]
#            l = key
#    st = ''
#    for key in hand.keys():
#        if key!=l:
#            st+=key
#    print(st)
#    for word in words:
#        #print(word)
#        if word in st:
#            print("in if")
#            print(word)
#            break       

#    print(random.sample(range(1, len(st)), 3))
#    s1 = random.sample(range(1, len(st)+1), len(words)-1)
#    while s1 =='':
#        s -= 1
#        words = by_size(wordList, s)
#        low = 20
#        for key in hand.keys():
#            if hand[key] < low:
#                low = hand[key]
#                l = key
#        st = ''
#        for key in hand.keys():
#            if key!=l:
#                st+=key
#        s1 = random.sample(range(1, len(st)+1), len(words))
##letters = set('aqk')
#    for word in words:
#        if s1 & set(word):
#            ls.append(word)
#    return ls

#hand = createHand()
#print(hand)
#return hint(hand)
#ls = hint(hand)
#print(ls)
