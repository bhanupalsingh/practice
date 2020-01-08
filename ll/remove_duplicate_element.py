
Given a sorted linked list, delete all duplicates such that each element appear only once. For example, Given 1->1->2, return 1->2. Given 1->1->2->3->3, return 1->2->3.



class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        
        
        if(A.next is None):
            return A;
            
            
        head1 = A;
        head2 = A.next;
       
        while(head2 is not None):
            while(head2 is not None and head2.val == head1.val ):
                head2 =  head2.next;
            head1.next = head2;
            head1 = head2;
            if(head2 is not None):
                head2 = head2.next;
            
        
        return A;
        
            
            
