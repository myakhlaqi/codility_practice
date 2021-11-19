#!/usr/bin/env python3
import re

def solution(N):
    #binary_n=bin(N)[2:]
    #binary_n=format(N,"b")
    binary_n="{0:b}".format(N)
    rx_pattern=r"010"
    binary_n=re.sub(rx_pattern,"0110",binary_n)
    result=re.findall(r"10+1",binary_n)
    #print(max([len(x)-2 for x in result]))
    return max([x.count("0") for x in result],default=0)
    
