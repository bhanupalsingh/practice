A sequence of integers is called nice if its elements are arranged in blocks like in [3, 3, 3, 4, 1, 1]. Formally, if two elements are equal, everything in between must also be equal. Let's define difficulty of a sequence as a minimum possible number of elements to change to get a nice sequence. However, if you change at least one element of value x to value y, you must also change all other elements of value x into y as well. For example, for [3, 3, 1, 3, 2, 1, 2] it isn't allowed to change first 1 to 3 and second 1 to 2. You need to leave 1's untouched or change them to the same value. Print difficulty of given sequence A of size N. Input Format:

Input 1:
    A = [3, 7, 3, 7, 3]
Output 1:
    2
Explanation:
    change both 7 to 3
Input 2:
    A = [3, 3, 7, 7, 7, 1]
Output 2:
    0
Input 3:
    A = [3, 3, 1, 3, 2, 1, 2]
Output 3:
    4

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        map = {};
        n = len(A);
        
        for i in range(n):
            if(A[i] in map):
                map[A[i]][1] = i;
            else:
                map[A[i]] = [i,i];
        
        #print(map);
        i=0;
        count = 0;
        while(i<n):
            j=map[A[i]][1];
            starti = i;
            countMap = {};
            maxsofar = 0;
            while(i<j):
                if(map[A[i]][1] > j):
                    j = map[A[i]][1];
                else:
                    if(A[i] in countMap):
                        countMap[A[i]] += 1;
                    else:
                        countMap[A[i]] = 1;
                        
                    maxsofar = max(maxsofar,countMap[A[i]]);
                    i += 1;
                    
                #print(i,j,count,countMap);
            
            if(i<n):
                if(A[i] in countMap):
                    countMap[A[i]] += 1;
                else:
                    countMap[A[i]] = 1;
            maxsofar = max(maxsofar,countMap[A[i]]);    
            
            i+=1;
            count += (i-starti-maxsofar);
            #print(countMap,i,starti,maxsofar);
        
        
        return count;
            
            
