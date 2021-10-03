


def balance_paranthesis(string):
    stack=[]

    i=0
    remove={}
    for i,c in enumerate(string):
        if c=="(":
            stack.append(i)
        elif c==")":
            if len(stack)==0:
                remove[i]=1
            else:
                stack.pop()

    while len(stack)!=0:
        index=stack.pop()
        remove[index]=1

    out=""
    for i in range(len(string)):
        if i not in remove:
            out=out+string[i]
    return out


string="((sgag(sdf(agdsg)fdsf)"
print balance_paranthesis(string)
