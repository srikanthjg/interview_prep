
def getLine(p1,p2):
    m = float((p2[1]-p1[1])/(p2[0]-p1[0]))
    c = float(p2[1] - (m*p2[0]))
    #print "y-"+str(m)+"x-"+str(c)
    #print m,c
    return (m,c)

#1 ABOVE
#0 ON
#-1 BELOW
#input ==> line = (m,c)
def isOnLine(line,pt):
    #y-mx-c
    sol = pt[1]-(line[0]*pt[0] )-line[1]
    #print "sol=%d"%sol
    if(sol>0):
        return 1
    elif sol ==0:
        return 0
    else:
        return -1

def isPointInTriangle(tri,pt):
    ## Get 3 lines from tri
    ## check if pt lies 1> (below 2 lines and above one line) or 2> (above 2lines and below one line)

    lines = []

    ## Get 3 lines from tri
    lines.append(getLine(tri[0],tri[1]))
    lines.append(getLine(tri[0],tri[2]))
    lines.append(getLine(tri[1],tri[2]))
    #print lines

    # if pt on one of the lines return true
    #if(isOnLine(lines[0],pt) or isOnLine(lines[1],pt) or isOnLine(lines[2],pt)):
    #    return 1

    ## check if pt lies 1> (below 2 lines and above one line) or 2> (above 2lines and below one line)
    if(  (isOnLine(lines[0],pt)==-1 and isOnLine(lines[1],pt)==-1 and isOnLine(lines[2],pt)==1) or
         (isOnLine(lines[0],pt)==1 and isOnLine(lines[1],pt)==1 and isOnLine(lines[2],pt)==-1) ):
         return 1

    return 0


tri = [(0,0),(5,5),(10,0)]
pt = (6,6)

#line =(1,0)
#print isOnLine(line,[1,2])
print isPointInTriangle(tri,pt)
