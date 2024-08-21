class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        seen = dict()

        A.sort()

        result = set()

        for i in xrange(len(A)):
            for j in xrange(i+1, len(A)):
                curr_sum = A[i] + A[j]
                diff = B - curr_sum
                if diff in seen:
                    for prev_sum in seen[diff]:
                        if A[prev_sum[1]] <= A[i] and i > prev_sum[1]:
                            result.add((A[prev_sum[0]], A[prev_sum[1]], A[i], A[j]))

                if curr_sum in seen:
                    seen[curr_sum].append((i, j))
                else:
                    seen[curr_sum] = [(i, j)]

        return sorted([list(item) for item in result])

#reduce to 2 sum by keeping 1 constant
    def threesum(self,A,target):
        output = []
        for i in range(len(A)):
            cur_sum = target-A[i]
            map = {}
            for j in range(i+1,len(A)):
                if (cur_sum-A[j]) not in map:
                    map[A[j]] = 0
                if(cur_sum-A[j] in map):
                    output.append([A[i],A[j],cur_sum-A[j]])
        return output



a = [4,3,7,1,2,9,11]
b = 20

sol = Solution()
print sol.threesum(a,b)
#print sol.fourSum(a,b)
