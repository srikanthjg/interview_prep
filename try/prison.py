def nextDay(states):

    next1=[0 for i in range(len(states))]
    next1[0]=0^states[1]
    next1[-1]=0^states[len(states)-2]
    for i in range(1,len(states)-1):
        if states[i-1]==states[i+1]:
            next1[i]=0
        else:
            next1[i]=1
    return next1

def cellCompete(states, days):
    # WRITE YOUR CODE HERE

    memo={}

    day=0
    prev=states
    cycle=False
    while day<days:
        next_cell=nextDay(prev)
        prev=next_cell
        #print next_cell
        t=tuple(next_cell)
        if t not in memo:
            memo[tuple(t)]=1
        else:
            cycle=True
            break
        day+=1

    if cycle:
        days=days%(day-1)
        for i in range(days):
            next_cell=nextDay(prev)
            prev=next_cell

    return next_cell
states=[1,1,1,1,1,1,1,1]
days=1
print cellCompete(states,days)
