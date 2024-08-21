def is_valid_soduku(A):
    soduku = []
    if(len(A)!=9):
        return 0
    #îprint A
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            if len(A[i])!=9:
                return 0
            print A[i]
            if A[i]== ".":
                row.append(-1)
            else:
                row.append(int(A[i][j]))
        soduku.append(row)
    print soduku



    return 1


A = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
print is_valid_soduku(A)
