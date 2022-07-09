# Problem: Consider n coins aligned in a row. Each coin is showing heads at the beginning.
# 1 2 3 4 5 6 7 8 9 10 
# Then, n people turn over corresponding coins as follows. Person i reverses coins with numbers
# that are multiples of i. That is, person i flips coins i, 2 · i, 3 · i, . . . until no more appropriate
# coins remain. The goal is to count the number of coins showing tails. In the above example,
# the final configuration is

import math

def coins(n):
    """ O(N*log(N))"""
    result = 0
    coin = [0 for i in range(n+1)]
    for i in range(1, n+1):
        k = i
        while (k <= n):
            if(k % i == 0):
                coin[k] = (coin[k]+1) % 2
            k += i
        result += coin[i]

    return result


def coins2(n):
    """ O(N)"""
    result = 0
    coin = [0 for i in range(n+1)]
    for i in range(1, n+1):
        if(int(math.sqrt(i))*int(math.sqrt(i)) == i):
            result += 1
    return result

print(coins( 100))
print(coins2(100))
