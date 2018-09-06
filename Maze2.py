raw=input()
n=int(raw.split(' ')[0])
m=int(raw.split(' ')[1])
maze=[]
for x in range(n):
    text=input()
    maze.append(text)

deadCount=0
adjacent=[[1,1]]
taken=[]
while(len(adjacent)>0):
    if adjacent[0] in taken:
        adjacent.pop(0)
        continue
    
    x=adjacent[0][0]
    y=adjacent[0][1]
    taken.append(adjacent[0])
    #counting walls for one position
    walls=0
    if maze[x][y]==".":
        #counting walls
        try:
            if maze[x-1][y]=="%":
                walls=walls+1
        except:
            pass
        try:
            if maze[x][y-1]=="%":
                walls=walls+1
        except:
            pass
        try:
            if maze[x][y+1]=="%":
                walls=walls+1
        except:
            pass
        try:
            if maze[x+1][y]=="%":
                walls=walls+1
        except:
            pass
        if(walls==3):
            deadCount=deadCount+1

        #recording adjacent paths
        try:
            if maze[x-1][y]==".":
                adjacent.append([x-1,y])
        except:
            pass
        try:
            if maze[x][y-1]==".":
                adjacent.append([x,y-1])
        except:
            pass
        try:
            if maze[x][y+1]==".":
                adjacent.append([x,y+1])
        except:
            pass
        try:
            if maze[x+1][y]==".":
                adjacent.append([x+1,y])
        except:
            pass

        #deleting present node from adjacent
        adjacent.pop(0)

print(deadCount)
