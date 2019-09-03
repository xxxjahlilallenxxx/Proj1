def lineCharacterCount(line):
    #Counts the characters that can fit on one line

def movesLeftMargin(startNum):
    #starts cursor at "" inch(es) on left Margin
    formatter.push_margin(startNum)
    
def marginProblem():
    #main function
    leftM = input("Please enter a number for left margin: ")
    rightM = input("Please enter a number for right margin: ")
    movesLeftMargin(leftM)
    finput = open('testFile.txt','r')
    finputList = finput.read()
    textFile = open('DAT1.txt','w')
    while len(finputList) > 0:
        if (len(finputList)) > 80:
            textFile.write(finputList[0:80])
            for x in range(0,80):
              finputList.pop()
        else:
            textFile.write(finputList)
    
