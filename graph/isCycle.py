
g={}
g[1]=[2,3]
g[2]=[3]
g[3]=[4]
g[4]=[]

visited={}
path={}
topo_sort=[]

def isCycle_helper(g,v):
    #print v
    if v in path:
        #Cycle found
        print "cycle found"
        return True

    path[v]=True
    for u in g[v]:
        if u not in visited:
            cycle=isCycle_helper(g,u)
            if cycle:
                return True
    topo_sort.insert(0,v)
    del path[v]
    visited[v]=True

    return False

def isCycle(g):
    for v in g.keys():
        if v not in visited:
            t=isCycle_helper(g,v)
            if t==True:
                return True

    return False

print isCycle(g)
print topo_sort
