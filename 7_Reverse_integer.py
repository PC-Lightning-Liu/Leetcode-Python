class Solution(object):
    def reverse(self, x):
        if x >= 0:
            ans = str(x)
            ans = list(ans)
            ans.reverse()
            ans = int(''.join(ans))
            if -1*pow(2,31) <= int(ans) <= pow(2,31)-1:
                return int(ans)
            else:
                return 0
        else:
            ans = str(x)
            ans = list(ans[1:])
            ans.reverse()
            ans = int(''.join(ans))
            if -1*pow(2,31) <= -1*int(ans) <= pow(2,31)-1:
                return -1*int(ans)
            else:
                return 0
            
        """
        :type x: int
        :rtype: int
        """
# 简写，本质差不多，不过好像cmp，和'`'貌似不能在python3里面使用

def reverse(self, x):
    s = cmp(x, 0)
    r = int(`s*x`[::-1])
    return s*r * (r < 2**31)
