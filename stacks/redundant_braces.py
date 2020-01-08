Input 1:
    A = "((a + b))"
Output 1:
    1
    Explanation 1:
        ((a + b)) has redundant braces so answer will be 1.

Input 2:
    A = "(a + (a + b))"
Output 2:
    0
    Explanation 2:
        (a + (a + b)) doesn't have have any redundant braces so answer will be 0.

class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        
        stack = ["NA"];
        n = len(A);
        i=0;
        
        sign = ["+","-","*","/"];
        
        while(i<n):
            
            
            if(A[i] == ")"):
                if(len(stack)>=4):
                    b=stack.pop();
                    s = stack.pop();
                    a = stack.pop();
                    start = stack.pop();
                    
                    if(s in sign and start == "(" ):
                        stack.append("z");
                    else:
                        return 1;
                        
                else:
                    return 1;
            
            else:
                stack.append(A[i]);
                
            i+=1;
            
            
           # if(A[i] == "+" or A[i] == "-" or A[i] == "*" or A[i] == "/"):
           #     stack.append(A[i]);
           #     while(i<n and A[i] != ")"):
           #         stack.append(A[i]);
           #         i += 1;
                    
           #     while(len(stack)>0 and stack[-1] != "("):
           #         stack.pop();
           #     if(len(stack)>0):
           #         stack.pop();
                
           #     if(len(stack)>0 and stack[-1] == "("):
           #         return 1;
           # else:
           #     stack.append(A[i]);
            
            
           # i+=1;
                
        
        return 0;

