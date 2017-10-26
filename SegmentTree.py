#307. Range Sum Query - Mutable
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        lennum = len(nums)
        if lennum == 0:
            return
        temp = lennum-1
        cnt = 0
        while temp:
            temp = temp >> 1
            cnt += 1
        newlen = 1 << cnt
        self.newlen = newlen
        self.sums = [0] * (newlen << 1)
        self.sums[newlen:newlen+lennum] = nums
        for i in range(newlen - 1, 0, -1):
            self.sums[i] = self.sums[i<<1]+self.sums[(i<<1)+1]
        self.ranges = [(0, 0) for i in range(newlen << 1)]
        for i in range((newlen << 1) - 1, newlen - 1, -1):
            self.ranges[i] = (i-newlen, i-newlen+1)
        for i in range(newlen - 1, 0, -1):
            self.ranges[i] = (self.ranges[i<<1][0], self.ranges[(i<<1)+1][1])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        tempid = i + self.newlen
        orival = self.sums[tempid]
        while tempid >= 1:
            self.sums[tempid] += val - orival
            tempid >>= 1
    
    def mysumRange(self, b, e, root):
        if self.ranges[root] == (b, e):
            return self.sums[root]
        mid = (self.ranges[root][0]+self.ranges[root][1])/2
        if e > mid and b < mid:
            return self.mysumRange(b, mid, root<<1) + self.mysumRange(mid, e, (root<<1)+1)
        elif e > mid:
            return self.mysumRange(b, e, (root<<1)+1)
        else:
            return self.mysumRange(b, e, root<<1)
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.mysumRange(i, j+1, 1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)