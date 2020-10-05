class Solution(object):
    def createTable(self,prices):
        table=[]

        for buyday in range(len(prices)):
            row=[0]*len(prices)
            for sellday in range(len(prices)):
                if buyday >= sellday:
                    row[sellday] = 0
                else:
                    row[sellday] = prices[sellday]-prices[buyday]
            table.append(row)
        return table

    def calcProfit(self,table):
        profit = 0
        dayProfit = 0
        days = len(table)

        for row in range(days):
            for col in range(days):
                if table[row][col] <=0:
                    continue
                dayProfit=[]

        if profit < 0:
            profit = 0

        return profit

    def maxProfit_dp(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        table = self.createTable(prices)
        return self.calcProfit(table)

    def maxProfit(self, prices):
        """
        local minima and local maxima approach
        """

        localMin = []
        localMax=[]

        i=0
        j=0
        k=0
        buy=0
        sell=0

        while(k<len(prices)-1):
            #localMin
            i=k
            j=i+1
            while(j<len(prices)-1):
                if(prices[i]>prices[j]):
                    i=i+1
                else:
                    buy=prices[i]
                    break
                j=j+1

            #buy on last day is not valid
            if i == len(prices)-1:
                return -1

            #localMax
            i=buy
            j=j+1
            while(j<len(prices)-1):
                if(prices[i]>prices[j]):
                    sell=i
                    break
                else:
                    j=j+1


            k=i+1
            print buy,sell




prices = [7,1,5,3,6,4]
sol=Solution()
print sol.maxProfit(prices)
