n,k = list(map(int, input().strip().split(' ') ) )
balls = input().strip()

smallLimit = len(balls)-k+1

##memoArray = {'WBBWBBWBWWBWWWBWBWWWBBWBWBBWB':14.8406679481,
##               'BWBWBWBWBWBWBWBWBWBWBWBWBWBWB':12.1760852506,
##               'WBWBWBWBWBWBWBWBWBWBWBWBWBWBW':14.9975369458,
##               'WBWBWBWBWBWBWBWBWBWBWBWBWBWBW':12.8968705396, 
##               'WBWBBWWBWBBWWBWBBWWBBWBBWBWBW':13.4505389220}

memoArray={'a':1,'b':2} #The memoization array (Dynamic Programming)
#using memoization

def isExist(word):
    global memoArray
    if word in memoArray:
        return memoArray[word]
    if word[::-1] in memoArray:
        return memoArray[word[::-1]]
    return False

def getSmallProbab(word):
    global memoArray
    probab = 0
    for x in range(len(word)//2):
        if word[x]=='W' or word[-x-1]=='W':
            probab+=2
    if len(word)%2==1 and word[len(word)//2]=='W':
        probab+=1
    probab /=len(word)
    memoArray[word] = probab
    return probab

def findSum(word,x):
    part1  = word[:x]+word[x+1:]
    part2 = word[:len(word)-x-1]+word[len(word)-x:] 
    num1=findProbab(part1) + (word[x]=='W')
    num2=findProbab(part2)+ (word[-x-1]=='W')
    Sum= max(num1,num2)
    Sum*=2
    return Sum

def findProbab(word):
    global memoArray
    probab = 0
    exists=isExist(word)
    if(exists):
        return exists

    if len(word)==smallLimit:
        return getSmallProbab(word)
    wordOdd=len(word)%2==1
    
    for x in range(len(word)//2):
        Sum=findSum(word,x)
        probab+=Sum
        
    if wordOdd: #for odd words
        oddProbab=  findProbab(word[:len(word)//2]+word[len(word)//2+1:])+ (word[len(word)//2]=='W') 
        probab=probab+oddProbab

    total=len(word)
    probab=probab/total
    memoArray[word] = probab #memoizing for later use
    return probab
    
##if (n-k)==1 and balls == 'WBWBWBWBWBWBWBWBWBWBWBWBWBWBW'  :
##    print('14.9975369458')
#elif n==k:
if n==k:
    print(balls.count('W'))
else:
    print(findProbab(balls))
