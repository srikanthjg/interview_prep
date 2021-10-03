def is_constraint_valid(a,b,c,n):
    return True if 1<=a<=b<=c and 4<=n<=7 else False

print(is_constraint_valid(1,2,3,1))
