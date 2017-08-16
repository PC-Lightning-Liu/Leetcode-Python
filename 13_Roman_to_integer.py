class Solution(object):
    def romanToInt(self, s):
        r = 0
        s = list(s)
        for i in range(len(s)):
            if s[i] == 'D':
                s[i]= 500
            elif s[i] == 'L':
                s[i]= 50
            elif s[i] == 'V':
                s[i]= 5
            elif s[i] == 'M':
                s[i]= 1000
            elif s[i] == 'C':
                s[i]= 100
            elif s[i] == 'X':
                s[i]= 10
            elif s[i] == 'I':
                s[i]= 1
        i = 0
        while i < len(s):
            if i+1 < len(s):
                if s[i] == 1 or s[i] == 10 or s[i] ==100:
                    if s[i+1] > s[i]:
                        r += s[i+1] - s[i]
                        i = i + 2
                    else: 
                        r = r+ s[i]
                        i +=1
                else: 
                    r = r+ s[i]
                    i +=1
            else:
                r = r + s[i]
                i +=1
        return r
        
        """
        :type s: str
        :rtype: int
        """
#感受来自大佬的蔑视吧

class Solution:
# @param {string} s
# @return {integer}
def romanToInt(self, s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]
