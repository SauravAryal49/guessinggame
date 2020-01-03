game=["dog", "cat", "rabbit"]
print("hint : three pet animals","and you have only five 'wrong' trials options")
guess=""
guess_number=0
number=[0,1,2]
guess_result = False
while (guess_number<5) and not(guess_result==True):
    guess=input("enter the guess")
    x=False
    for i in number:
        if (guess.strip()==game[i]):
            x=True
            print("thats correct")
            game.remove(game[i])
            number.pop()
            if (game==[]):
                print(":) you win congrats")
                guess_result=True
    if (x==True):
        continue
    else:
        print("not correct")
        guess_number+=1
if (guess_number==5):
    print(":( sorry you lost")



