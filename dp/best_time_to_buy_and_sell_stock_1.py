Best Time to Buy and Sell Stocks I

Say you have an array, A, for which the ith element is the price of a given stock on day i. If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit. Return the maximum possible profit. 
 Input Format:


Input 1:
    A = [1, 2]

Output 1:
    1

Explanation:
    Buy the stock on day 0, and sell it on day 1.

Input 2:
    A = [1, 4, 5, 2, 4]

Output 2:
    4

Explanation:
    Buy the stock on day 0, and sell it on day 2.
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProfit(self, A):
	    if(len(A)<2):
	        return 0;
	    i= 1;
	    buy = A[0];
	    maxprofit = 0;
	    n = len(A);
	    
	    
	    diff = 0;
	    minsofar = [A[i] for i in range(n)];
	    
	    
	    for i in range(1,n):
	        diff = max(A[i]-minsofar[i-1],diff);
	        minsofar[i] = min(minsofar[i-1],A[i]);
	        
	    return diff;
	   # while(i<n):
	   #     while(i<n and A[i]<A[i-1]):
	   #         i+=1;
	        
	   #     buy = A[i-1];
	   #     while(i<n and A[i]>A[i-1]):
	   #         i+=1;
	            
	   #     sell = A[i-1];
	        
	   #     maxprofit += (sell-buy);
	        
	    return maxprofit;
	        
	        

