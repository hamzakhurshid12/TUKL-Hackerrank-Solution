def stringStrip(value,index):
    return value[:index]+value[index+1:]

def compareValues(ballString,num):
    outputList=[]
    if (ballString[num]=='W'):
        outputList.append(stringStrip(ballString,num))
        if(ballString[len(ballString)-num]=='W'):
            return [1,[stringStrip(ballString,len(ballString)-num),outputList[0]]]
        else:
            return [1,[outputList[0]]]
    elif (ballString[len(ballString)-num]=='W'):
        return [1,[stringStrip(ballString,len(ballString)-num)]]
    else:
        return [0,[stringStrip(ballString,num),stringStrip(ballString,len(ballString)-num)]]
        #return [0,[]]

def checkString(ballString):
    countTotal=0
    countGood=0
    takenList=[]
    for x in range(1,len(ballString)): #iterating i
        tempList=compareValues(ballString,x)
        #print("for x="+str(x)+": ",tempList)
        for x in tempList[1]:
            if(x not in takenList):
                takenList.append(x)
                countTotal=countTotal+1
        countGood=countGood+int(tempList[0])
    return [countGood,len(ballString)-1,takenList]
                
def evaluate(word,iterations):
    probab=0
    tempVar=checkString(word)
    probab=float(probab)+float(tempVar[0])/float(tempVar[1])
    print(tempVar)
    newProcess=tempVar[2]
    print("At k=1, Total Probab=",probab)
    for k in range(1,iterations):
        tempProcess=[]
        total=0
        good=0
        for w in newProcess:
            print("For element: ",w)
            temp=checkString(w)
            print(temp)
            total=total+float(temp[1])
            good=good+float(temp[0])
            for x in temp[2]:
                #if x not in tempProcess:
                tempProcess.append(x)
        probab=probab+float(good)/float(total)
        print("At k="+str(k+1)+", Probab=",float(good)/float(total))
        newProcess=tempProcess
        print("next level")
    return probab

    
line1=input()
n=int(line1.split(' ')[0])
k=int(line1.split(' ')[1])
line2=' '+input()
#val=int(input())
#print(checkString(" BWBWW"))
print(evaluate(line2,k))
#print()
#for x in range(1,val+1):
#    print(compareValues(line2,x))
