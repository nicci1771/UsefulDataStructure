#recurisively
class Solution(object):
    def decode(self, s, i):
        res = ''
        slen = len(s)
        if slen == 0:
            return s, i
        while i < slen and s[i] != ']':
            if ord(s[i]) < ord('0') or ord(s[i]) > ord('9'):
                res += s[i]
                i += 1
            else:
                cnt = 0
                while i < slen and ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
                    cnt = cnt*10+ord(s[i])-ord('0')
                    i += 1
                i += 1
                t, i = self.decode(s, i)
                i += 1
                res += t * cnt
        return res, i
    
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.decode(s, 0)[0]

#iteratively using stack