Evaluate Expression To True
Given an expression, A, with operands and operators (OR , AND , XOR), in how many ways can you evaluate the expression to true, by grouping in different ways? Operands are only true and false. Return the number of ways to evaluate the expression modulo 103 + 3. 
 Input Format:
The first and the only argument of input will contain a string, A.

The string A, may contain these characters:
    '|' will represent or operator 
    '&' will represent and operator
    '^' will represent xor operator
    'T' will represent true operand
    'F' will false
Output:
Return an integer, representing the number of ways to evaluate the string.


Input 1:
    A = "T|F"

Output 1:
    1

Explanation 1:
    The only way to evaluate the expression is:
        => (T|F) = T 

Input 2:
    A = "T^T^F"

Output 2:
    0

Explanation 2:
    There is no way to evaluate A to a true statement.



class Solution:
    def countways(self,operand,operator,n):
        mod = 10**3+3
        T = [[0 for i in range(n+1)]for i in range(n+1)]
        F = [[0 for i in range(n+1)]for i in range(n+1)]
        
        for i in range(n):
            if operand[i]=='F':
                F[i][i] = 1
                T[i][i] = 0
            else:
                F[i][i] = 0
                T[i][i] = 1
        for gap in range(1,n):
            i = 0
            for j in range(gap,n):
                T[i][j] = F[i][j] = 0
                for g in range(gap):
                    k = i+g
                    tik = T[i][k]+F[i][k]
                    tkj = T[k+1][j]+F[k+1][j]
                    if operator[k] == '&': 
                        T[i][j] += T[i][k] * T[k + 1][j] 
                        F[i][j] += (tik * tkj - T[i][k] * T[k + 1][j]) 
                                             
                    if operator[k] == '|': 
                        F[i][j] += F[i][k] * F[k + 1][j] 
                        T[i][j] += (tik * tkj - F[i][k] * F[k + 1][j]) 
                                             
                    if operator[k]=='^': 
                        T[i][j] += (F[i][k] * T[k + 1][j] + T[i][k] * F[k + 1][j]) 
                                      
                        F[i][j] += (T[i][k] * T[k + 1][j] + F[i][k] * F[k + 1][j]) 
                                     
                i += 1
        return T[0][n-1]%mod;
    # @param A : string
    # @return an integer
    def cnttrue(self, A):
        n = len(A)
        operand = []
        operator = []
        for i in range(n):
            if A[i] == 'T' or A[i] == 'F':
                operand.append(A[i])
            else:
                operator.append(A[i])
        return self.countways(operand,operator,len(operand))
            
