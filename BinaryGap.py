#!/usr/bin/env python3
"""A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.
Write a function:
def solution(N)
that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.
For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..2,147,483,647].
"""
def to_binary(n):
    """convert integer values to binary list of

        Args:
            n (integer): integer numbers to

        Returns:
            list: list of 1 and 0 representing binary value
        """
    list=[]
    while n!=0:
        list.insert(0,n%2)
        n=n//2
    return list

def solution(N):
    """This function get and integer number as input and count the max length of consequence number of zeros
    Args:
        N (Integer): input number
    Returns:
        [integer]: maxmal number of consequence zeros
    """
    binary=to_binary(N)
    j=0
    max=0
    j=0
    i=1
    zero=0
    while(j<len(binary)):
        while(binary[i]!=1):
            zero=zero+1
            i=i+1
            if(i==len(binary)):
                zero=0
                break
        if(zero>max):
            max=zero
        zero=0
        i=i+1
        j=i
    return max
    
print("max is ", solution(20))
