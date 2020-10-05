def isConsecutive(l1,l2,B):
    #print "yes"

    if l1[1]+B+1==l2[0]:
        return True
    else:
        return False

def maxone(A,B):
    index=[]
    pair=[]
    for i in range(len(A)):
        ##get 1s in A :start,end
        #start index
        if  (A[i]==1 and i==0) or (A[i]==1 and A[i-1]==0) :
            start=i
            pair.append(start)

        #end index
        if (A[i==1] and i==len(A)-1) or (A[i]==1 and A[i+1]==0) :
            end = i
            pair.append(end)
            index.append(pair)
            pair = []
    #print index

    #retain consecutive pairs in index
    # end1 + 2 = start2
    if len(index)<=1:
        #print "return"
        return -1
    #remove non-consecutive
    for i in range(1,len(index)-1):
        #print i,index[i]
        if (isConsecutive(index[i-1],index[i],B) == False) and (isConsecutive(index[i],index[i+1],B) == False):
            del index[i]
    if len(index)<=1:
        #print "return"
        return -1
    if not isConsecutive(index[len(index)-2],index[len(index)-1],B):
        del index[-1]

    #print index
    maxlen=0
    maxlist_index=0
    for l in range(len(index)):
        if len(index[l]) >maxlen:
            maxlen=len(index[l])
            maxlist_index=l

    if isConsecutive(index[maxlist_index-1],index[maxlist_index],B):
        start=index[maxlist_index-1][0]
        end=index[maxlist_index][1]
    elif isConsecutive(index[maxlist_index],index[maxlist_index+1],B):
        start=index[maxlist_index][0]
        end=index[maxlist_index+1][1]

    #return start,end
    output=[0]*(end-start+1)
    for i in range(end-start+1):
        output[i]=start
        start+=1
    return output

A = [1,1,1,1 ,1 ,0 ,1 ,1 ,0,0,1 ,1 ,1 ,0,1]
B=1
print maxone(A,B)
