class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #so my logic for this one would be I either want to hold what the profit is at the moment and what number we would for a certain index to hold a higher profit. Data structure I would use idk maybe a dict
        #keep track of lowest left number
        lowest_left = prices[0]
        max_profit = 0
        
        for num in prices:
            #new lowest possible buy price is all the matter from now
            if num < lowest_left:
                lowest_left = num
            #profit check if selling on this day from a new lowest or a new high
            todays_profit = num - lowest_left
            if todays_profit > max_profit:
                max_profit = todays_profit
        return max_profit

            

