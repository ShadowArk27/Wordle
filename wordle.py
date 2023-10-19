
#------- LIBRARIES ------#
import sys
import random
try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")


with open ("words.txt", "r") as wordFile:
    dic = wordFile.readlines()

#------- VARIABLES -------#

green = "STRING"
yellow = "KEYWORD"
black = "TODO"
red = "ERROR"


#-------- FUNCTIONS ---------#
def split(word):
    return list(word)

def reset():
    word = random.choice(dic)
    #print(word)
    #dic.remove(word)
    words = list(word)
    words.remove('\n')
    word = listToString(words)
    #print(words)
    tries = 0
    print(word)
    

def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1
    

#-------- MAIN CODE --------#

#dic = ['fades', 'storm', 'great',  'prayer', 'bread', 'share', 'stale', 'glare']


word = random.choice(dic)
#print(word)
#dic.remove(word)
words = list(word)
words.remove('\n')
word = listToString(words)
#print(words)

running = True
tries = 0

while 1 == 1:
    x = input("What is your guess: ")
    x = str(x)
    word = str(word)

    if x == "help":
        print(word)
    
    
    
    elif len(list(x)) == 5:

        if (x + '\n') in dic:
            tries += 1
            
            guessList = list(x) 
            for letter in list(x):
                if letter in word:
                    #print(guessList.index(letter))
                    #print(word.index(letter))
                    if guessList.index(letter) == word.index(letter):
                        color.write(letter, green)
                        print('')
                    else:
                        color.write(letter, yellow)
                        print('')
                else:
                    color.write(letter, black)
                    print('')
        else:
            print("Invalid Entry")
            print('')
        

    else:
        print('\nHas to be 5 letters :/')

    print('')

    if x == word:
        print('CONGRATS YOU GOT IT!!!\n')
        print(f'It took you {tries} turns')
        print('')
        word = random.choice(dic)
        words = list(word)
        words.remove('\n')
        word = listToString(words)
        tries = 0

        


        
        
