Input 1:
    A = "myinterviewtrainer",
    B = ["trainer", "my", "interview"]

Output 1:
    1

Explanation 1:
    Return 1 ( corresponding to true ) because "myinterviewtrainer" can be segmented as "my interview trainer".

Input 2:
    A = "a"
    B = ["aaa"]

Output 2:
    0

Explanation 2:
    Return 0 ( corresponding to false ) because "a" cannot be segmented as "aaa".








import sys;
sys.setrecursionlimit(10500)


class Solution:
	# @param A : string
	# @param B : list of strings
	# @return an integer
	
	def recur(self,start,A,B,memo):
	    
	    
	    
	    n = len(A);
	    
	    if(start in memo):
	        return memo[start];
	    if(start >= n):
	        return True;
	    for i in range(start+1,n+1):
	        temp = A[start:i];
	        #print(temp);
	        if(temp in B and self.recur(i,A,B,memo) == True):
	            #print(temp);
	            memo[start] = True;
	            return True;
	    
	    memo[start]  = False;
	    return False;
	        
	
	def wordBreak(self, A, B):
        memo = {};
        if(self.recur(0,A,B,memo)==True):
            return 1;
        else:
            return 0;
