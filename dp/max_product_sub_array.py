Input : [2, 3, -2, 4]
Return : 6 

Possible with [2, 3]

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        
        dpma = [A[i] for i in range(len(A))];
        dpmi = [A[i] for i in range(len(A))];
        maxproduct = A[0];
        
        n = len(A);
        for i in range(1,n):
            dpma[i] = max(A[i]*dpma[i-1],A[i]*dpmi[i-1]);
            if(dpma[i]<=0):
                dpma[i] = A[i];
            dpmi[i] = min(A[i]*dpma[i-1],A[i]*dpmi[i-1]);
            if(dpmi[i]>=0):
                dpmi[i] = A[i];
                
                
            
                
            
           
            
            maxproduct = max(dpma[i],maxproduct);
            
            #print(dpma,dpmi);
        return maxproduct;
           
