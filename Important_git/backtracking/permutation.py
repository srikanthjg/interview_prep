################################################################################
def permutation_swap(str_list):
    #print "A,index,i"
    permutation_swap_helper(str_list,0)

def permutation_swap_helper(A,index):
    #print "  "*index,
    #print A,index,
    #print "",
    if(index == len(A)-1):
        print A
        return

    for i in range(len(A)):
        #print i
        A[i],A[index] = A[index],A[i]
        permutation_swap_helper(A,index+1)
        A[i],A[index] = A[index],A[i]

    return

################################################################################
def permutation_rec_helper1(chosen,rest):
    if len(rest)==0:
        print "".join(chosen)
        return

    for i in range(len(rest)):
        chosen.append(rest[i])
        tmp = rest.pop(i)
        permutation_rec_helper1(chosen,rest)
        chosen.pop()
        rest.insert(i,tmp)



def permutation_rec1(A):
    permutation_rec_helper1([],A)
    return

################################ BEST ##########################################
## PERMUTATION ##
output=[]
def permutation_rec_helper2(combo,input_string):
    #print combo,input_string
    if(len(combo)==3):
        print combo
        output.append(combo)
        return

    for letter in input_string:
        permutation_rec_helper2(combo+letter,input_string)

def permutation_rec2(A):
    permutation_rec_helper2("",A)
    return

A = "abc"
#permutation_swap(list(A))
print permutation_rec1(list(A))
