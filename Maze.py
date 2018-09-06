raw=input()
n=int(raw.split(' ')[0])
m=int(raw.split(' ')[1])
mazeList=[]
deadEnds=0
for x in range(n):
    text=input()
    mazeList.append(text)

adj=[[1,1]]
gotten=[]
while(len(adj)>0):
    sides=0
    if(adj[0] not in gotten):
        x=adj[0][0]
        y=adj[0][1]
        if mazeList[x][y]==".":
            if mazeList[x-1][y]=="%":
                sides+=1
            if mazeList[x][y-1]=="%":
                sides+=1
            if mazeList[x][y+1]=="%":
                sides+=1
            if mazeList[x+1][y]=="%":
                sides+=1
            if(sides>=3):
                deadEnds=deadEnds+1
            #adding adjacent nodes into array
            gotten.append(adj[0])
            adj.pop(0)
            if mazeList[x-1][y]==".":
                adj.append([x-1,y])
            if mazeList[x][y-1]==".":
                adj.append([x,y-1])
            if mazeList[x][y+1]==".":
                adj.append([x,y+1])
            if mazeList[x+1][y]==".":
                adj.append([x+1,y])
    else:
        adj.pop(0)
print(deadEnds)
