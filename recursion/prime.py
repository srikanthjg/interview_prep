out=[]
def solve_helper(input,depth,product):
    if depth == 3:
        out.append(product)
        return
    if product != 1:
        out.append(product)
    for i in input:
        solve_helper(input,depth+1,product*i)



def solve(A, B, C, D):
    input = [A,B,C]
    output=[]
    solve_helper(input,0,1)
    return

solve(2,3,5,5)
s = sorted(set(out))
print s[:5]
