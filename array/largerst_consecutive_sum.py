## kadane 's algorithm'

def largest_cont_sum(a):
    max_sum = a[0]
    prev_sum = a[0]

    #print "current sum before cal %r"%max_sum
    for i in range(len(a)):
        cur_sum = a[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
        for j in range(i+1,len(a)):
            if cur_sum > max_sum:
                max_sum = cur_sum

            cur_sum = cur_sum + a[j]
            prev_sum = cur_sum
            #print "current sum after cal %r"%cur_sum
            if cur_sum > max_sum:
                    max_sum = cur_sum
                    #print "max %d"%max_sum
                    continue
            elif cur_sum < prev_sum:
                    break
            #print "\n"
    return max_sum


print largest_cont_sum([1,2,-1,3,4,10,10,-10,-1])
