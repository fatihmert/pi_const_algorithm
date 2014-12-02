#-*- coding: utf-8 -*-

# Author:    Fatih Mert Doğancan
# Date:      02.12.2014

def arccot(x, u):
    sum = ussu = u // x
    n = 3
    sign = -1
    while 1:
        ussu = ussu // (x*x)
        term = ussu // n
        if not term:
            break
        sum += sign * term
        sign = -sign
        n += 2
    return sum

def pi(basamak):
    u = 10**(basamak+10)
    pi = 4 * (4*arccot(5,u) - arccot(239,u))
    return pi // 10**10

if __name__ == "__main__":
    print pi(1000) # 1000 basamaklı bi sayısı

