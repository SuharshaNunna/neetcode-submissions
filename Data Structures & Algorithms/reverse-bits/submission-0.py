class Solution:
    def reverseBits(self, n: int) -> int:
        # int not iterable so convert to string, put in stack, then convernt stack  to int
        # reverse not FLIP 
        binary = bin(n)[2:].zfill(32)
        return int(binary[::-1], 2)