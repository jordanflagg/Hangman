

#guess = input()

#print(guess)


from cgitb import html
from mimetypes import guess_all_extensions
from re import T
from urllib.request import urlopen
html = urlopen("https://www.mit.edu/~ecprice/wordlist.10000").read()
#print(html)

import random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

#response = urllib.urlopen(word_site)

WORDS = html.splitlines()

word = random.choice(WORDS)

if len(word) <= 5:
    word = random.choice(WORDS)

#print(word)
#print(type(word))

word = word.decode("utf-8")
#print(type(word))


#for letter in word:
    #print(str(letter))
    #print(type(letter))




print("BEGIN")

wrong = 0
glist = []
display = []
word_list = []


for letter in word:
    display.append("_")
    word_list.append(letter)
   
    
print(display)

i = 0

while wrong <= 10:

    
    guess = input()
    glist.append(guess)
    
    print(glist)
    
    i = 0
    correct = False

    for letter in word_list:
        

        
        if guess == letter:
            correct = True
            display[i] = guess

            
        i += 1
            

    if correct:
        print("Right!")
        if "_" not in display:
                print("WINNER")
                break
    else:
        print("Nope!")
        wrong += 1

    if wrong == 0:
        
        print(    "   _____     \n"
                  "  |     |    \n"
                  "  |     |    \n"
                  "  |          \n"
                  "  |          \n"
                  "  |          \n"
                  "  |          \n"
                  "__|__        \n")
            

    elif wrong == 1:
        
        print(    "   _____     \n"
                  "  |     |    \n"
                  "  |     |    \n"
                  "  |     0    \n"
                  "  |          \n"
                  "  |          \n"
                  "  |          \n"
                  "__|__        \n")
        

    elif wrong == 2:
        
        print(    "   _____     \n"
                  "  |     |    \n"
                  "  |     |    \n"
                  "  |     0    \n"
                  "  |     |    \n"
                  "  |          \n"
                  "  |          \n"
                  "__|__        \n")

    elif wrong == 3:
        
        print(    "   _____     \n"
                  "  |     |    \n"
                  "  |     |    \n"
                  "  |     0    \n"
                  "  |    -|    \n"
                  "  |          \n"
                  "  |          \n"
                  "__|__        \n")

    elif wrong == 4:
        
        print(    "   _____     \n"
                  "  |     |    \n"
                  "  |     |    \n"
                  "  |     0    \n"
                  "  |   o-|    \n"
                  "  |          \n"
                  "  |          \n"
                  "__|__        \n")

    elif wrong == 5:
        
        print(    "   _____     \n"
                  "  |     |    \n"
                  "  |     |    \n"
                  "  |     0    \n"
                  "  |   o-|-   \n"
                  "  |          \n"
                  "  |          \n"
                  "__|__        \n")

    elif wrong == 6:
        
        print(    "   _____     \n"
                  "  |     |    \n"
                  "  |     |    \n"
                  "  |     0    \n"
                  "  |   o-|-o  \n"
                  "  |          \n"
                  "  |          \n"
                  "__|__        \n")

    elif wrong == 7:
        
        print(    "   _____     \n"
                  "  |     |    \n"
                  "  |     |    \n"
                  "  |     0    \n"
                  "  |   o-|-o  \n"
                  "  |    /     \n"
                  "  |          \n"
                  "__|__        \n")                                                       
            
    elif wrong == 8:
        
        print(    "   _____     \n"
                  "  |     |    \n"
                  "  |     |    \n"
                  "  |     0    \n"
                  "  |   o-|-o  \n"
                  "  |    /     \n"
                  "  |          \n"
                  "__|__        \n")

    elif wrong == 9:
        
        print(    "   _____     \n"
                  "  |     |    \n"
                  "  |     |    \n"
                  "  |     0    \n"
                  "  |   o-|-o  \n"
                  "  |    /     \n"
                  "  |   ~      \n"
                  "__|__        \n")   

    elif wrong == 10:
        
        print(    "   _____     \n"
                  "  |     |    \n"
                  "  |     |    \n"
                  "  |     0    \n"
                  "  |   o-|-o  \n"
                  "  |    / \   \n"
                  "  |   ~      \n"
                  "__|__        \n")   

    elif wrong == 11:
        
        print(    "   _____     \n"
                  "  |     |    \n"
                  "  |     |    \n"
                  "  |     0    \n"
                  "  |   o-|-o  \n"
                  "  |    / \   \n"
                  "  |   ~   ~  \n"
                  "__|__        \n")         

        print("GAME OVER")                                     

    correct = False        
    print(str(11-wrong) + " guesses left")
    print(display)
              

print(word)
