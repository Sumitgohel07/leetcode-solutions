class Solution:
    def reverse(self, x: int) -> int:
        output = 0
        flage = 0
        if x < 0:
            flage = 1
            x = -(x)
        while(x > 0):
            reminder = x % 10
            output = (output*10 + reminder)
            x = x//10
        output =  output if flage==0 else -(output)
        if output >= -(2**31) and output <= ((2**31)-1):
            return output
        else:
            return 0