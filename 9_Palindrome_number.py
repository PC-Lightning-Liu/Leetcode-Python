class Solution(object):
    def isPalindrome(self, x):
        if x == 0:
            return True
        elif x < 0:
            return False
        i = 1
        temp = 0
        while pow(10,i) <= x:
            i += 1
        a = x
        for j in range(i):
            temp = temp + (a % 10) * pow(10, i-j-1)
            a = (a-(a % 10)) / 10 
        if temp == x:
            return True
        else:
            return False
        
        """
        :type x: int
        :rtype: bool
        """
# 这是一种写法，就是构造一个反向的数，还有一种是依次对比最前和最后两个，第二种方法比较快，因为没必要完全构造出来一个新的数

class Solution:
    # @param x, an integer
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False

        ranger = 1
        while x / ranger >= 10:
            ranger *= 10

        while x:
            left = x / ranger
            right = x % 10
            if left != right:
                return False
            
            x = (x % ranger) / 10
            ranger /= 100

        return True
