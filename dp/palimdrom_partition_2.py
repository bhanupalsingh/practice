Palindrome Partitioning II
Palindrome Partitioning II
Given a string A, partition A such that every substring of the partition is a palindrome. Return the minimum cuts needed for a palindrome partitioning of A. 
 Input Format:
The first and the only argument contains the string A.
Output Format:
Return an integer, representing the answer as described in the problem statement.


Input 1:
    A = "aba"

Output 1:
    0

Explanation 1:
    "aba" is already a palindrome, so no cuts are needed.

Input 2:
    A = "aab"

Output 2:
    1

Explanation 2:
    Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.class Solution:
	# @param A : string
	# @return an integer
	
	
	def palimdrom(self,A,pali):
	    n = len(A);
	    for i in range(n):
	        pali[i][i] = True;
	    
	    for l in range(2,n+1):
	        for i in range(0,n-l+1):
	            j = i+l-1;
	            
	            if(A[i]==A[j]):
	                if(l==2 or pali[i+1][j-1]==True):
	                    pali[i][j] = True;
	            else:
	                pali[i][j] = False;
	    
	    
	    
	    
	def minCut(self, A):
	    n = len(A);
	    
	    pali = [[False for i in range(n)] for j in range(n)];
	    
	    self.palimdrom(A,pali);
	    memo = {};
	    res = [float("inf")];
	    
	    
	    C = [0]*(n+1);
	    for i in range(n): 
            if (pali[0][i] == True): 
                C[i] = 0; 
            else: 
                C[i] = sys.maxsize; 
                for j in range(i): 
                    if(pali[j + 1][i] == True and 1 + C[j] < C[i]): 
                        C[i] = 1 + C[j]; 
                        
        return C[n-1];
      
    
	    
	    
	    
	    
	    
	    
	    
	    if(pali[0][n-1] == True):
	        return 0;
	    self.recur(0,A,pali,memo,res);
	    
	    return res[0];
	    
	
	def recur(self,start,A,B,memo,res):
	    n = len(A);
	   # if(start in memo):
	   #     return memo[start];
	    if(start >= n-1):
	        return 0;
	        
	    for i in range(start,n):
	        if(B[start][i] == True):
	            if(i==n-1 or i == n):
	                return 0;
	            else:
	                res[0] =  min(res[0], 1 + self.recur(i+1,A,B,memo,res))
	            
	        #print(A[start:i+1],res[0],start,i);    
	        
	            #print(A[start:i+1],memo[start]);
	    #return memo[start];
	    
	    
	    return n-start-1;
	    
	   # temp = n-start-1;
	   # memo[start]  = temp;
	   # return temp;
	        
	

	    
	    
