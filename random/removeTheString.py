Remove the Substring
Given 2 strings of lowercase alphabets A and B of size N and M respectively. it is guaranteed that B is a subsequence of A.

For example, the strings "test", "tst", "tt", "et" and "" are subsequences of the string "test". But the strings "tset", "se", "contest" are not subsequences of the string "test".


Input 1:
    A = "bbaba"
    B = "bb"
Output 1:
    3
Explaination 1:
    A[2::4] = "aba" can be removed and B still remains the subsequence of A[0::1]


Input 2:
    A = "bbaba"
    B = "ab"
Output 2:
    2


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        
        n = len(A);
        m = len(B);
        
        
        pre = [0 for i in range(n+2)];
        post = [0 for i in range(n+2)];
        temp = [i for i in range(n+2)];
        
        
        i=0;
        j=0;
        
        
        #prefix sum
        count  = 0;
        while(i<n):
            if(j<m):
                if(A[i]==B[j]):
                    j += 1;
                    count +=1;
            i += 1;
            pre[i] = count; 
                    
            
        #postfix sum
        count  = 0;
        i=n-1;
        j=m-1;
        while(i>=0):
            if(j>-1):
                if(A[i]==B[j]):
                    j -= 1;
                    count +=1;
            
            post[i+1] = count;
            i -= 1;
        
        
        result = 0;
        j=0;
            
        for i in range(0,n+2):
            while(j<n+2):
                if(pre[i]+post[j] == m):
                   result = max(result,j-i-1);
                   if(j<n+1 and post[j] != post[j+1]):
                       break;
                j += 1;
        return result;
                
                
        
        
        print(pre);
        print(post);
        print(temp);
        
        
        
        
        
        
        
        
        

