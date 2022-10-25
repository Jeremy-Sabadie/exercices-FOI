redPrint="Dans une zone rouge"
yellowPrint="Dans une zone jaune"
bluePrint="Dans une zone bleue"
outPrint="En dehors de la feuille"


tokens=int(input())
for a in range(tokens):
    abs=int(input())
    ord=int(input())
  #conditions for the first of two areas in red.
    firstRedConditions=(abs>15 and abs<45) and (ord>60 and ord<70)
  #conditions for second of two areas in red.
    secondRedConditions=(abs>60 and abs<85) and (ord>60 and ord<70)
  #conditions for the square aera in yellow.
    squareYellowConditions=(abs>25 and abs<50) and (ord>20 and ord<45)
  #conditions for the blue zones
    blueConditions=(abs>10 and abs<85) and (ord>10 and ord<55) and not(squareYellowConditions)
  #conditions for the remaining aeras in yellow.
    bigYellowConditions=(abs>0 and abs<90) and (ord>0 and ord<70) and not(blueConditions) and not(firstRedConditions) and not(secondRedConditions)
    if firstRedConditions or secondRedConditions:
        print(redPrint)
    elif blueConditions:
        print(bluePrint)
    elif squareYellowConditions or bigYellowConditions:
        print(yellowPrint)
    else:
        print(outPrint)



