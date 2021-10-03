output=[]
def generateParanthesisHelper(n,combo):
    #print combo
    if n%2!=0:
        return

    if len(combo)==(n):
        output.append(combo)
        return

    generateParanthesisHelper(n,"("+combo+")")
    generateParanthesisHelper(n,"("+")"+combo)
    generateParanthesisHelper(n,combo+"("+")")


def generateParanthesis(n):
        generateParanthesisHelper(n,"")
        return


def isSubSequence(str1,str2):
    m = len(str1)
    n = len(str2)

    j = 0
    i = 0

    while i<n and j<m:
        if str1[j] == str2[i]:
            j = j+1
        i = i + 1

    return j==m

def checkInvalid(string):
    stack=[]
    invalid=0
    for s in string:
        if len(stack)==0 and s==")":
            invalid+=1
            continue
        if s=="(":
            stack.append(s)
        else:
            stack.pop()
    return invalid

def remove_paranthesis(string):

    invalid=checkInvalid(string)
    generateParanthesis(len(string)-invalid)
    res=[]
    for s in output:
        if isSubSequence(s, string):
            res.append(s)
    return res

string="()())()"
res=remove_paranthesis(string)
print set(res)
