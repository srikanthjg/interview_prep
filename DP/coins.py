#https://leetcode.com/problems/coin-change/submissions/
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[[-1 for i in range(amount+1)] for j in range(len(coins))]
        #print dp

        for j in range(len(dp[0])):
            if j%coins[0]==0:
                dp[0][j]=j//coins[0]
            else:
                dp[0][j]=float('inf')

        for i in range(1,len(dp)):
            for j in range(len(dp[0])):
                if j<coins[i]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=min(1+dp[i][j-coins[i]],dp[i-1][j])
        #print dp
        out=dp[len(coins)-1][amount]
        if out==float('inf'):
            return -1
        else:
            return out



    def helper_without_memo(self,sum,coins,amount,level):
        if sum>amount:
            return float('inf')

        if sum==amount:
            return level

        q=float('inf')
        for c in coins:
            q=min(q,self.helper_without_memo(sum+c, coins, amount, level+1))
        return q


    memo={}
    ##Bottom UP
    def helper_memo_b(self,coins,amount):
        if amount in self.memo:
            return self.memo[amount]

        if amount<0:
            self.memo[amount]=float('inf')
            return float('inf')

        if amount==0:
            self.memo[amount]=0
            return 0

        q=float('inf')
        for c in coins:
            q=min(q,1+self.helper_memo_b(coins, amount-c))
        self.memo[amount]=q
        return self.memo[amount]


    ###BESTTTT
    def helper_memo_b_2(self,sum,coins,amount):
        if sum in self.memo:
            return self.memo[sum]
        if sum==amount:
            return 1
        if sum>amount:
            return 0

        q=float('inf')
        for c in coins:
            q=min(q,1+self.helper_memo_b_2(sum+c,coins,amount))
        self.memo[sum]=q
        return q

    def helper_memo_t(self,sum,coins,amount,level):
        if sum in self.memo:
            return self.memo[sum]
        if sum>amount:
            self.memo[sum]=float('inf')
            return float('inf')
        if sum==amount:
            self.memo[sum]=level
            return level

        q=float('inf')
        for c in coins:
            sum1=sum+c
            q=min(q,self.helper_memo_t(sum1, coins, amount, level+1))
        self.memo[sum1]=q
        return q

    def coinChange_memo(self,coins,amount):
        level=0
        sum=0
        #coins.sort(reverse=True)
        return self.helper_memo_b_2(sum,coins,amount)
        #return self.helper_memo_b(coins,amount)

sol=Solution()
coins=[1,2,5]
amount=11

print "out=%r"%sol.coinChange_memo(coins, amount)
print sol.memo
