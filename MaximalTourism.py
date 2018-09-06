import sys

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
route = []
for route_i in range(m):
	route_t = [int(route_temp) for route_temp in input().strip().split(' ')]
	route.append(route_t)

##Mycode Starts here
def getAdjacentNodes(node):
    nodes=[]
    for x in range(len(paths)):
        if(paths[x][0]==node) and paths[x][1] not in nodes:
            nodes.append(paths[x][1])
    return nodes

paths=[]
for x in range(m):
    if not route[x][0]==route[x][1]:
        paths.append(route[x])
        paths.append([route[x][1],route[x][0]])

count=[0]
allTaken=[]
for x in range(1,n+1):
    count.append(0)
    if x in allTaken:
        continue
    taken=[]
    #print("X is:",x)
    adjacent=getAdjacentNodes(x)
    taken.append(x)
    count[x]=count[x]+1
    while(len(adjacent)>0):
        if adjacent[0] not in taken:
            count[x]=count[x]+1
            taken.append(adjacent[0])
            adj2=getAdjacentNodes(adjacent[0])
            allTaken.append(adjacent[0])
            adjacent.pop(0)
            for y in adj2:
                if y not in adjacent:
                    adjacent.append(y)
            #print(adjacent)
        else:
            adjacent.pop(0)

print(max(count))
        
