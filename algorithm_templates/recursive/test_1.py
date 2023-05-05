
# 心得：
# 主要想清楚几点问题就行了 
# 1.这个问题的子问题是什么。
# 2.当前层要干什么事情。
# 3.递归出口 【边界条件】

# 很多刚接触递归的同学习惯往深处想，就想想清楚下一层，
# 下下层到底咋回事，千万别！
# 这样永远也想不清楚的，
# 你只要把当前层的事情干好，
# 边界条件找好，
# 深层自然而然就是对的。


# 231 :https://leetcode.cn/problems/power-of-two/description/
# 2 的幂

class Solution:
    def isPowerOfTwo(self, n) -> bool:
        if n == 1:
            return True
        if n <= 0 or int(n) != n:
            return False
        else: ##开始递归
            return self.isPowerOfTwo(n / 2)


## 算阶乘
def jiecheng(x):
  # sum=1
  # while x>0:
  #   sum=x*jiecheng(x-1)
  #   x-=1
  # if x==0:
  #   return 1
  # return sum
  if x==0:
  	return 1
  else: ##开始递归
  	return x*jiecheng(x-1)


## 个位想加
## https://leetcode.cn/problems/add-digits/description/
# 输入: num = 38
# 输出: 2 
# 解释: 各位相加的过程为：
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# 由于 2 是一位数，所以返回 2。

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        new_num = reduce(lambda x,y:x+y,map(int,list(str(num))))
        if num>=10: ##开始递归
            return self.addDigits(new_num)
        else:
            return reduce(lambda x,y:x+y,map(int,list(str(num))))

