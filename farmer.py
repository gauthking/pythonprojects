
"""THIS CODE IS STILL UNDER DEVELOPMENT"""

print("A FARMER WITH A FOX, A GOOSE AND A SACK OF GRAINS WANT TO CROSS THE RIVER FROM EAST TO WEST SIDE.\nBut unfortunately the boat can allow only the farmer and one of his possessions.\nSolve this task of transporting the farmer and his items to the west side of the river.\nAnd yeah ITS NOT AN EASY TASK, CHECK THE HINT BELOW FOR MORE INFO XD:")
print("The farmer is on the east side with fox,grain and the goose. INPUT the possession to be taken by the farmer")
print("\n\n")
print("The farmer is allowed to take one possession with him during the journey from either side")
print("Hint: THINK ABOUT THE FOOD CHAIN HERE XD\n")
print("*****INPUT VALUES TAKEN********\nFOX\nGOOSE\nGRAIN\nNONE")
c=0
score=0
while c==0:
    n=input("Enter the Possession:")
    if n.upper()=="FOX":
        print("WRONG CHOICE!! THE GOOSE EATS GRAIN")
        score-=1
        print("ONE POINT DEDUCTED:X")
    elif n.upper()=="GRAIN":
        print("WRONG CHOICE!! THE FOX EATS THE GOOSE lololololXD")
        score-=1
        print("ONE POINT DEDUCTED:X")
    elif n.upper()=="GOOSE":
        print("CORRECT!! Everyone's Safe")
        c+=1
        score+=1
        print("YOU'VE GOT ONE POINT")
    else:
        print("invalid")
print("NOW THE GOOSE HAS REACHED THE WEST ALONG WITH FARMER ")
print("\n")
print("NOW THE FARMER HAS TO RETURN TO EAST FOR BRINGING THE OTHER ITEMS\n")
print("FARMER HAS THE OPTION TO TAKE SOMETHING FROM THE DEPART POINT AND TO DROP AT THE DESTINATION POINT")
s = 0
while s==0:
    n3 = input("Enter the take from the west:")
    n2 = input("Enter the drop at west from east:")
    if n2.upper() == "GRAIN" and n3.upper() == "GOOSE":
        print("CORRECT CHOICE!! YOU EARNED ONE POINT")
        score+=1
        print("EAST SIDE:FOX BOAT:GOOSE \n WEST SIDE:GRAIN")
        n5 = input("Enter the take from east:")
        n4 = input("Enter the drop at east from west:")
        if n4.upper() == "GOOSE" and n5.upper() == "FOX":
            print("CORRECT CHOICE!! YOU EARNED TWO POINTS")
            score+=2
            print("EAST SIDE:GOOSE \n WEST SIDE: GRAIN BOAT:FOX")
            n7 = input("Enter the take from west:")
            n6 = input("Enter the drop at west from east:")
            if n6.upper() == "GOOSE" and n7.upper() == "NONE":
                print("CORRECT CHOICE!! ALL ARE SAFE!!")
                print("YOU'VE EARNED 5 POINTS WOOH!!")
                score+=5
                s += 1
            else:
                print("WRONG CHOICE")
                print("ONE POINT DEDUCTED:X")
                score-=1

        else:
            print("Wrong Choice")
            print("ONE POINT DEDUCTED:X")
            

    else:
        print("wrong choice")
        print("ONE POINT DEDUCTED:X")


if score>3:
    print("YOU'VE SURPASSED THE MINIMUM SCORE, CONGRATULATIONS!!!\nYOURSCORE=",score)
else:
    print("You've got points below the MIN SCORE which is 3 YOURSCORE=",score,"MINSCORE=3")
