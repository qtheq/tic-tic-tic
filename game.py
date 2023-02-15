#####################---------------------------------##################### 
#####################-------- tic tic tic >:3 --------##################### 
#####################---------------------------------##################### 

print("\ntic tac toe!! if you don't know the rules, simply leave <3 \n")

## main display
## sets up strings for display and later manipulation (yes i know some are repeats, it's easier to have it set up by line (i can't think))
line1   = "----------------------------------"
line2   = "#L |  |  A  |  |  B  |  |  C  |  |"
line3   = "   |  |-----|--|-----|--|-----|  |"
line4   = "   |  |-----|--|-----|--|-----|  |"
nl1     = "1  |  |  {}  |  |  {}  |  |  {}  |  |"
line6   = "   |  |-----|--|-----|--|-----|  |"
line7   = "   |  |-----|--|-----|--|-----|  |"
nl2     = "2  |  |  {}  |  |  {}  |  |  {}  |  |"
line9   = "   |  |-----|--|-----|--|-----|  |"
line10  = "   |  |-----|--|-----|--|-----|  |"
nl3     = "3  |  |  {}  |  |  {}  |  |  {}  |  |"
line12  = "   |  |-----|--|-----|--|-----|  |"
line13  = "----------------------------------"

blank = " "
Xdisp = "X"
Odisp = "O"

print(line1, line2, line3, line4, 
      nl1.format(blank, blank, blank), 
      line6, line7, 
      nl2.format(blank, blank, blank), 
      line9, line10, 
      nl3.format(blank, blank, blank), 
      line12, line13, sep = "\n")

## these are made as separate versions of the variables specifcally for printing
## this way the board stays even and {} doesn't display
nl1p = str(nl1.format(blank, blank, blank))
nl2p = str(nl2.format(blank, blank, blank))
nl3p = str(nl3.format(blank, blank, blank))

print("first, pick if you want to be X's or O's. whoever is the second player will be the opposite (they don't get free will)")
print("then enter the letter of where you want to put your piece, and enter the number in the next line")

prevplay = []
prevrow = []
xplay = []
oplay = []

## checks if the input for the marker is correct (and insults you otherwise)
## also sets the values to be consistent in case the case differs
## cxo exists for the first check for switching players to make sure the switch doesn't occur on the first turn
correct = False
while correct == False:
    cxo = input("X's or O's?:")

    if (cxo == "x") or (cxo == "X"):
        cxo = "x"
        xo = "x"
        correct = True
    elif (cxo =="o") or (cxo == "O"):
        cxo = "o"
        xo = "o"
        correct = True
    else:
        print("put in an 'X' or an 'O,' stupid")
        correct = False

turn = 1

## GAME STARTS
playing = True
while playing == True:
    
## switches players
    if (cxo == "x") and (xo == "x") and (turn != 1):
        xo = "o"
        cxo = "o"
    elif (cxo == "o") and (xo == "o") and (turn != 1):
        xo = "x"
        cxo = "x"

## checks to make sure the input is valid and is a new play
    new = False
    while new == False:
        correct = False
        while correct == False:
            let = input("Letter:")
            if (let == "a") or (let == "A"):
                let = "a"
                correct = True
            elif (let =="b") or (let == "B"):
                let = "b"
                correct = True
            elif (let =="c") or (let == "C"):
                let = "c"
                correct = True
            else:
                print("put in an 'A,' 'B,' or 'C,' idiot")
                correct = False    

        correct = False
        while correct == False:
            try:
                num = int(input("Number:"))
            
                if (num == 1) or (num == 2) or (num == 3):
                    correct = True
                else:
                    print("put in '1,' '2,' or '3,' loser")
            except ValueError:
                print("put in '1,' '2,' or '3,' loser")
        
        play = let + str(num)
        
        if (play in prevplay):
            print("this spot has been used already!!! stop!!!")
            new = False
        else:
            new = True
           
## game part...
    print(line1, line2, line3, line4, sep = "\n", end = "\n")

## PREVIOUS PLAY CHECKS
## these are checked by row to ensure the board doesn't visually break at any point
    if (num in prevrow):
        if (num == 1):
            
## FOR A1
            if (let == "a"):
    ## B1 & C1
                if (xo == "x"):
                    nl1p = str(nl1.format(Xdisp, blank))
                    nl1 = str(nl1.format(Xdisp, {}))
                    print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
                elif (xo == "o"):
                    nl1p = str(nl1.format(Odisp, blank))
                    nl1 = str(nl1.format(Odisp, {}))
                    print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
## FOR B1                    
            if (let == "b"):
    ## BOTH A1 AND C1 FILLED
                if ("a1" in prevplay) and ("c1" in prevplay):    
                    if (xo == "x"):
                        nl1p = str(nl1.format(Xdisp))
                        nl1 = str(nl1.format(Xdisp))
                        print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
                    elif (xo == "o"):
                        nl1p = str(nl1.format(Odisp))
                        nl1 = str(nl1.format(Odisp))
                        print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
    ## A1
                if (xo == "x") and ("a1" in prevplay) and ("c1" not in prevplay):
                    nl1p = str(nl1.format(Xdisp, blank))
                    nl1 = str(nl1.format(Xdisp, {}))
                    print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
                elif (xo == "o") and ("a1" in prevplay) and ("c1" not in prevplay):
                    nl1p = str(nl1.format(Odisp, blank))
                    nl1 = str(nl1.format(Odisp, {}))
                    print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
    ## C1
                if (xo == "x") and ("c1" in prevplay) and ("a1" not in prevplay):
                    nl1p = str(nl1.format(blank, Xdisp))
                    nl1 = str(nl1.format({}, Xdisp))
                    print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
                elif (xo == "o") and ("c1" in prevplay) and ("a1" not in prevplay):
                    nl1p = str(nl1.format(blank, Odisp))
                    nl1 = str(nl1.format({}, Odisp))
                    print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
## FOR C1                    
            if (let == "c"):
    ## BOTH A1 AND B1 FILLED
                if ("a1" in prevplay) and ("b1" in prevplay):    
                    if (xo == "x"):
                        nl1p = str(nl1.format(Xdisp))
                        nl1 = str(nl1.format(Xdisp))
                        print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
                    elif (xo == "o"):
                        nl1p = str(nl1.format(Odisp))
                        nl1 = str(nl1.format(Odisp))
                        print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
    ## A1 & B1
                else:
                    if (xo == "x"):
                        nl1p = str(nl1.format(blank, Xdisp))
                        nl1 = str(nl1.format({}, Xdisp))
                        print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
                    elif (xo == "o"):
                        nl1p = str(nl1.format(blank, Odisp))
                        nl1 = str(nl1.format({}, Odisp))
                        print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
                     
        if (num == 2):
   
## FOR A2
            if (let == "a"):
    ## B2 & C2
                if (xo == "x"):
                    nl2p = str(nl2.format(Xdisp, blank))
                    nl2 = str(nl2.format(Xdisp, {}))
                    print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
                elif (xo == "o"):
                    nl2p = str(nl2.format(Odisp, blank))
                    nl2 = str(nl2.format(Odisp, {}))
                    print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
## FOR B2                    
            if (let == "b"):
    ## BOTH A2 AND C2 FILLED
                if ("a2" in prevplay) and ("c2" in prevplay):    
                    if (xo == "x"):
                        nl2p = str(nl2.format(Xdisp))
                        nl2 = str(nl2.format(Xdisp))
                        print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
                    elif (xo == "o"):
                        nl2p = str(nl2.format(Odisp))
                        nl2 = str(nl2.format(Odisp))
                        print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
    ## A2
                if (xo == "x") and ("a2" in prevplay) and ("c2" not in prevplay):
                    nl2p = str(nl2.format(Xdisp, blank))
                    nl2 = str(nl2.format(Xdisp, {}))
                    print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
                elif (xo == "o") and ("a2" in prevplay) and ("c2" not in prevplay):
                    nl2p = str(nl2.format(Odisp, blank))
                    nl2 = str(nl2.format(Odisp, {}))
                    print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
    ## C2
                if (xo == "x") and ("c2" in prevplay) and ("a2" not in prevplay):
                    nl2p = str(nl2.format(blank, Xdisp))
                    nl2 = str(nl2.format({}, Xdisp))
                    print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
                elif (xo == "o") and ("c2" in prevplay) and ("a2" not in prevplay):
                    nl2p = str(nl2.format(blank, Odisp))
                    nl2 = str(nl2.format({}, Odisp))
                    print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
## FOR C2                    
            if (let == "c"):
    ## BOTH A2 AND B2 FILLED
                if ("a2" in prevplay) and ("b2" in prevplay):    
                    if (xo == "x"):
                        nl2p = str(nl2.format(Xdisp))
                        nl2 = str(nl2.format(Xdisp))
                        print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
                    elif (xo == "o"):
                        nl2p = str(nl2.format(Odisp))
                        nl2 = str(nl2.format(Odisp))
                        print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
    ## A2 & B2
                else:
                    if (xo == "x"):
                        nl2p = str(nl2.format(blank, Xdisp))
                        nl2 = str(nl2.format({}, Xdisp))
                        print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
                    elif (xo == "o"):
                        nl2p = str(nl2.format(blank, Odisp))
                        nl2 = str(nl2.format({}, Odisp))
                        print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")                  
                    
        if (num == 3):
   
## FOR A3
            if (let == "a"):
    ## B3 & C3
                if (xo == "x"):
                    nl3p = str(nl3.format(Xdisp, blank))
                    nl3 = str(nl3.format(Xdisp, {}))
                    print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
                elif (xo == "o"):
                    nl3p = str(nl3.format(Odisp, blank))
                    nl3 = str(nl3.format(Odisp, {}))
                    print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
## FOR B3                    
            if (let == "b"):
    ## BOTH A3 AND C3 FILLED
                if ("a3" in prevplay) and ("c3" in prevplay):    
                    if (xo == "x"):
                        nl3p = str(nl3.format(Xdisp))
                        nl3 = str(nl3.format(Xdisp))
                        print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
                    elif (xo == "o"):
                        nl3p = str(nl3.format(Odisp))
                        nl3 = str(nl3.format(Odisp))
                        print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
    ## A3
                if (xo == "x") and ("a3" in prevplay) and ("c3" not in prevplay):
                    nl3p = str(nl3.format(Xdisp, blank))
                    nl3 = str(nl3.format(Xdisp, {}))
                    print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
                elif (xo == "o") and ("a3" in prevplay) and ("c3" not in prevplay):
                    nl3p = str(nl3.format(Odisp, blank))
                    nl3 = str(nl3.format(Odisp, {}))
                    print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
    ## C3
                if (xo == "x") and ("c3" in prevplay) and ("a3" not in prevplay):
                    nl3p = str(nl3.format(blank, Xdisp))
                    nl3 = str(nl3.format({}, Xdisp))
                    print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
                elif (xo == "o") and ("c3" in prevplay) and ("a3" not in prevplay):
                    nl3p = str(nl3.format(blank, Odisp))
                    nl3 = str(nl3.format({}, Odisp))
                    print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
## FOR C3                    
            if (let == "c"):
    ## BOTH A3 AND B3 FILLED
                if ("a3" in prevplay) and ("b3" in prevplay):    
                    if (xo == "x"):
                        nl3p = str(nl3.format(Xdisp))
                        nl3 = str(nl3.format(Xdisp))
                        print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
                    elif (xo == "o"):
                        nl3p = str(nl3.format(Odisp))
                        nl3 = str(nl3.format(Odisp))
                        print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
    ## A3 & B3
                else:
                    if (xo == "x"):
                        nl3p = str(nl3.format(blank, Xdisp))
                        nl3 = str(nl3.format({}, Xdisp))
                        print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
                    elif (xo == "o"):
                        nl3p = str(nl3.format(blank, Odisp))
                        nl3 = str(nl3.format({}, Odisp))
                        print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
                    
## FIRST PLAY IN ROW              
## ROW 1
    elif (num == 1):
## COLUMN A
        if (let == "a"):
            if (xo == "x"):
                nl1p = str(nl1.format(Xdisp, blank, blank))
                nl1 = str(nl1.format(Xdisp, {}, {}))
                print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
            else:
                nl1p = str(nl1.format(Odisp, blank, blank))
                nl1 = str(nl1.format(Odisp, {}, {}))
                print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
## COLUMN B
        if (let == "b"):
            if (xo == "x"):
                nl1p = str(nl1.format(blank, Xdisp, blank))
                nl1 = str(nl1.format({}, Xdisp, {}))
                print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
            else:
                nl1p = str(nl1.format(blank, Odisp, blank))
                nl1 = str(nl1.format({}, Odisp, {}))
                print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
## COLUMN C
        if (let == "c"):
            if (xo == "x"):
                nl1p = str(nl1.format(blank, blank, Xdisp))
                nl1 = str(nl1.format({}, {}, Xdisp))
                print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
            else:
                nl1p = str(nl1.format(blank, blank, Odisp))
                nl1 = str(nl1.format({}, {}, Odisp))
                print(nl1p, line6, line7, nl2p, line9, line10, nl3p, sep = "\n", end = "\n")

## ROW 2
    elif (num == 2):
        print(nl1p, line6, line7, sep = "\n", end = "\n")
## COLUMN A
        if (let == "a"):
            if (xo == "x"):
                nl2p = str(nl2.format(Xdisp, blank, blank))
                nl2 = str(nl2.format(Xdisp, {}, {}))
                print(nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
            else:
                nl2p = str(nl2.format(Odisp, blank, blank))
                nl2 = str(nl2.format(Odisp, {}, {}))
                print(nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
## COLUMN B
        if (let == "b"):
            if (xo == "x"):
                nl2p = str(nl2.format(blank, Xdisp, blank))
                nl2 = str(nl2.format({}, Xdisp, {}))
                print(nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
            else:
                nl2p = str(nl2.format(blank, Odisp, blank))
                nl2 = str(nl2.format({}, Odisp, {}))
                print(nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
## COLUMN C
        if (let == "c"):
            if (xo == "x"):
                nl2p = str(nl2.format(blank, blank, Xdisp))
                nl2 = str(nl2.format({}, {}, Xdisp))
                print(nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
            else:
                nl2p = str(nl2.format(blank, blank, Odisp))
                nl2 = str(nl2.format({}, {}, Odisp))
                print(nl2p, line9, line10, nl3p, sep = "\n", end = "\n")
                
## ROW 3
    elif (num == 3):
        print(nl1p, line6, line7, nl2p, line9, line10, sep = "\n", end = "\n")
## COLUMN A
        if (let == "a"):
            if (xo == "x"):
                nl3p = str(nl3.format(Xdisp, blank, blank))
                nl3 = str(nl3.format(Xdisp, {}, {}))
                print(nl3p)
            else:
                nl3p = str(nl3.format(Odisp, blank, blank))
                nl3 = str(nl3.format(Odisp, {}, {}))
                print(nl3p)
## COLUMN B
        if (let == "b"):
            if (xo == "x"):
                nl3p = str(nl3.format(blank, Xdisp, blank))
                nl3 = str(nl3.format({}, Xdisp, {}))
                print(nl3p)
            else:
                nl3p = str(nl3.format(blank, Odisp, blank))
                nl3 = str(nl3.format({}, Odisp, {}))
                print(nl3p)
## COLUMN C
        if (let == "c"):
            if (xo == "x"):
                nl3p = str(nl3.format(blank, blank, Xdisp))
                nl3 = str(nl3.format({}, {}, Xdisp))
                print(nl3p)
            else:
                nl3p = str(nl3.format(blank, blank, Odisp))
                nl3 = str(nl3.format({}, {}, Odisp))
                print(nl3p)

    print(line12, line13, sep = "\n", end = "\n")

## adds plays to lists in order to perform win checks and previous play checks 
    if (cxo == "x"):
        xplay.append(play)
    else:
        oplay.append(play)

    prevplay.append(play)
    prevrow.append(num)  
    
## HORIZONTAL CHECKS FOR WIN
    if (("a1" in xplay) and ("b1" in xplay) and ("c1" in xplay)):
        print("X won!!!!!!!")
        playing = False
    elif (("a1" in oplay) and ("b1" in oplay) and ("c1" in oplay)):
        print("O won!!!!!!!")
        playing = False

## VERTICAL CHECKS FOR WIN   
    if ((("a1" in xplay) and ("a2" in xplay) and ("a3" in xplay)) or (("b1" in xplay) and ("b2" in xplay) and ("b3" in xplay)) or (("c1" in xplay) and ("c2" in xplay) and ("c3" in xplay))):
        print("X won!!!!!!!")
        playing = False
    elif ((("a1" in oplay) and ("a2" in oplay) and ("a3" in oplay)) or (("b1" in oplay) and ("b2" in oplay) and ("b3" in oplay)) or (("c1" in oplay) and ("c2" in oplay) and ("c3" in oplay))):
        print("O won!!!!!!!")
        playing = False

## DIAGONAL CHECKS FOR WIN
    if (("a1" in xplay) and ("b2" in xplay) and ("c3" in xplay)):
        print("X won!!!!!!!")
        playing = False
    elif (("a1" in oplay) and ("b2" in oplay) and ("c3" in oplay)):
        print("O won!!!!!!!")
        playing = False
    
    if (("a3" in xplay) and ("b2" in xplay) and ("c1" in xplay)):
        print("X won!!!!!!!")
        playing = False
    elif (("a3" in oplay) and ("b2" in oplay) and ("c1" in oplay)):
        print("O won!!!!!!!")
        playing = False

## CHECK FOR FULL BOARD
    if (len(prevplay) == 9):
        print("you BOTH lost!!! HOW'D YOU DO THAT??????")

    turn += 1
