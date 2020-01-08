Coin Sum Infinite

Input : 
    S = [1, 2, 3] 
    N = 4

Return : 4

Explanation : The 4 possible ways are
{1, 1, 1, 1}
{1, 1, 2}
{2, 2}
{1, 3}    
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def coinchange2(self, A, B):

        dp = [0 for i in range(B+1)];
        
        dp[0] = 1;
       
        m = len(A);
        n = len(dp);
        for i  in range(m):
            for j in range(1,n):
                if(j>= A[i]):
                    dp[j] +=  dp[j-A[i]];
        
        #print(dp);
        return dp[-1]% 1000007;
    
