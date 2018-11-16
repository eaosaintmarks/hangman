#this is my superperb awesome non violent HANG THE MANNNNNNN GAME
from turtle import *
from random import randint
import time


import math

words= ["saint marks school water bottle", "trample me", "im not ok" \
, "sign out", 'Sialoquent', \
"Arachibutyrophobia", "odd flex", 'pneumonoultramicroscopicsilicovolcanoconiosis'\
'Awkward', 'Bagpipes', 'Banjo', 'Bungler', 'Croquet', 'Crypt', 'Dwarves', 'Fervid','Fishhook'\
, 'Fjord Gazebo', 'Gypsy', 'Haiku', 'Haphazard', 'Hyphen', 'Ivory', 'Jazzy', 'Jiffy', 'Jinx'\
, 'Jukebox', 'Kayak', 'Kiosk', 'Klutz', 'Memento', 'Mystify', 'Numbskull', 'Ostracize', 
'Oxygen', 'Pajama', 'Phlegm', 'Pixel', 'Polka', 'Quad', 'Quip', 'Rhythmic', 'Rogue' \
, 'Sphinx', 'Squawk', 'Swivel', 'Toady', 'Twelfth', 'Unzip', 'Waxy', 'Wildebeest'\
'Yacht', 'Zealous','Zigzag', 'Zippy','Zombie']

sWidth = 600
sHeight = 800
s = getscreen()
s.setup(sWidth, sHeight)
s.bgcolor('#baefeb')

t=getturtle()
t.color('#f7f199')
t.width(8)
t.speed(0)


tWriter = Turtle()
tWriter.hideturtle()
tWriter.shape('turtle')
tBadLetters = Turtle()
tBadLetters.hideturtle()
#secertWord= ""
#displayWord= ""
#fails = 6
#fontS= int(sHeight*0.05)

alpha= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ:"
displayWord= ""
secretWord= ""
lettersWrong=""
lettersCorrect=""
fails=6
fontS = int(sHeight*0.03)
gameDown = False 


def displayText(newText):
    tWriter.clear()
    tWriter.color('#fffdb2')
    tWriter.penup()
    tWriter.goto(-int(sWidth*0.4), -int(sHeight*0.375) )
    tWriter.write( newText, font=('Arial', fontS, 'bold') )


def displayBadLetters(newText):
    tBadLetters.clear()
    tBadLetters.color('#fffdb2')
    tBadLetters.penup()
    tBadLetters.goto(-int(sWidth*0.4), int(sHeight*0.375) )
    tBadLetters.write( newText, font=('Arial', fontS, 'bold') )




def chooseWord():
    global secretWord
    secretWord = words[randint(0, len(words) - 1)]
    print("The secret word is: " + secretWord)

def makeDisplay():
    global displayWord, secretWord
    displayWord = ""
    for letter in secretWord:
        if letter in alpha:
            if letter.lower() in lettersCorrect.lower():
                displayWord += letter + " "
            else:
                displayWord += "_" + " "
            

        else:
            displayWord += letter + " "

def getGuess():
    boxTitle = "letters Used:" + lettersWrong
    guess = s.textinput(boxTitle, "Enter a guess or type $$ to guess the word")
    return guess

def checkWordGuess():
    global gameDone, fails
    boxTitle = "Guess the WOrd"
    guess = s.textinput(boxTitle, "Enter your guess for the word...")
    if guess.lower() == secretWord.lower():
        displayText("THATS RIGHT! " + secretWord + " is the word!!")
        gameDone = True
    else:
        displayText("im sorry your guess of " + guess + " is wrong")
        time.sleep(1)
        displayText(displayWord)
        fails-=1
        updateHangmanPerson()


def updateHangmanPerson():
    global fails
    if fails == 5:
        drawHead()
    if fails == 4:
        drawBody()
    if fails == 3:
        drawLeftArm()
    if fails == 2:
        drawRightArm()
    if fails == 1:
        drawLeftLeg()
    if fails == 0:
        drawRightLeg()
        
def playGame():
    global fails, lettersCorrect, lettersWrong, alpha, gameDone
    while gameDown == False and fails > 0 and "_" in displayWord:
        theGuess = getGuess()
        print("The Guess is " + theGuess)
        if theGuess == "$$":
            checkWordGuess()
        elif len(theGuess) > 1 or theGuess == "":
            displayText("No!!! " + theGuess + " only one letter, please")
            time.sleep(1)
            displayText(displayWord)
        elif theGuess not in alpha:
            displayText('no!!!' + theGuess + " is not a letter.")
            time.sleep(1)
            displayText(displayWord)
            #we know itS a letter now
        elif theGuess.lower() in secretWord.lower():
            lettersCorrect += theGuess.lower()
            makeDisplay()
            displayText(displayWord)
        elif theGuess not in lettersWrong:
            displayText("no!!! " + theGuess + " Is not in the word!!!")
            time.sleep(1)
            lettersWrong += theGuess.lower() + ","
            displayBadLetters("Not in word: {" + lettersWrong + "}")
            #lettersWrong += theGuess.lower()
            displayText(displayWord)
            fails-=1
            updateHangmanPerson()
        else:
            displayText(theGuess + "is already guessed")
            time.sleep(1)
            displayText(displayWord)
        if fails<= 0:
            displayBadLetters("no more guesses")
            displayText("you lose. word is: " + secertWord)
            gameDone= True
        if "_" not in displayWord:
            displayBadLetters("you got it!")
            gameDone = True
    

def drawGallows():
    t.penup()
    t.setheading(0)
    t.goto(-int(sWidth*0.25), -int(sHeight*0.25)) 
    t.pendown()
    t.forward(int(sWidth*0.5))

    t.left(180)
    t.forward(60)
    t.right(90)
    t.forward(420)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(50)

def drawHead():
    hr = int(sWidth*0.09)
    t.penup()
    t.goto(t.xcor()-hr, t.ycor()- hr)
    t.pendown()
    t.circle(hr)

def drawBody():
    hr = int(sWidth*0.09)
#set up for body
    t.penup()
    t.goto(t.xcor()+hr, t.ycor()-hr)
#drawing body
    t.pendown()
    t.forward(150)

def drawLeftArm():
#setup for left arm
    t.penup()
    t.left(180)
    t.forward(90)
    t.pendown()
#drawing left arm
    t.left(50)
    t.forward(100)

def drawRightArm():
#setup for right arm
   
    t.penup()
    t.backward(100)
    t.pendown()
   
#drawing right arm
    t.right(100)
    t.forward(100)
    t.pendown()

def drawLeftLeg():
#setup
    t.penup()
    t.backward(100)
    t.right(130)
    t.pendown()
#drawing
    t.forward(100)
    t.left(30) 
    t.forward(100)

def drawRightLeg():
#setup
    t.penup()
    t.backward(100)
    t.pendown()
#drawing
    t.right(60)
    t.forward(100)


    
   
#Program starts here
drawGallows()
drawHead()
drawBody()
drawLeftArm()
drawRightArm()
drawLeftLeg()
drawRightLeg()
hideturtle()

#start playing game
time.sleep(1)
t.clear()
drawGallows()
chooseWord()
makeDisplay()
displayBadLetters("not in word: {" + lettersWrong + "}")
displayText(displayWord)
playGame()
