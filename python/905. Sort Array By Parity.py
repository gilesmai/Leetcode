class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even=list()
        odd=list()
        for num in A:
            if num%2==0:
                even.append(num)
            else :
                odd.append(num)
        return even+odd
        
