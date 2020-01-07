N digit numbers with digit sum S

N = 2, S = 4
Valid numbers are {22, 31, 13, 40}


import sys;
sys.setrecursionlimit(10000);


lookup = [[-1 for i in range(1001)]  
              for i in range(1001)]
              
              
class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	
	def recur(self,A,B,sumsofar,mapdata):
	    if(A==0 and sumsofar == B):
	        return 1;
	    if(sumsofar == B):
	        return 1;
	        
	    if(A<=0):
	        return 0;
	        
	    if(sumsofar > B):
	        return 0;
	        
        if (lookup[A][B-sumsofar] != -1): 
            return lookup[A][B-sumsofar] 
      
	    #key = str(A)+"-"+str(B-sumsofar);
	    #if(key in mapdata):
	        #return  mapdata[key];
	        
	    temp = 0;
	    for i in range(10):
	        if(sumsofar+i<=B):
	            temp += self.recur(A-1,B,sumsofar+i,mapdata);
	            
	    lookup[A][B-sumsofar]  = temp;
	    #mapdata[key] = temp;
	    return temp;
	
	 
  
    def countRec(self,n, Sum): 
      
        if (n == 0): 
            return Sum == 0
      
        if (lookup[n][Sum] != -1): 
            return lookup[n][Sum] 
      
        ans = 0
      
        for i in range(10): 
            if (Sum-i >= 0): 
                ans += self.countRec(n - 1, Sum-i) 
        lookup[n][Sum] = ans      
      
        return lookup[n][Sum] 
  

	
	def solve(self, A, B):
	    
	    
	   # ans = 0
    #     Sum = B;
    #     for i in range(1, 10): 
    #         if (Sum - i >= 0): 
    #             ans += self.countRec(A - 1, Sum - i) 
    #     return ans %1000000007
        
	    res = [0];
	    mapdata = {};
	    for i in range(1,10):
	        res[0] += self.recur(A-1,B,i,mapdata);
	        
	    return res[0]%1000000007;

