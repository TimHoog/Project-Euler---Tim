from math import sqrt
import prime

def eulerchallenge1():
    i = 0
    #Check which numbers are divisible by 3 or 5 and add them together
    for x in range(1, 1000):
        if x % 3 == 0 or x % 5 == 0:
            i = i + x
    return i


def eulerchallenge2():
    i=0
    fiblist = [1, 2]
    while fiblist [-1] <= 4000000:
        fiblist.append(fiblist[-1] + fiblist[-2])
    fiblist.pop()
    for x in fiblist:
        if x % 2 == 0:
            i = i + x
    return i


def eulerchallenge3(): 
    #we need to calculate the highest prime factor of the following very large number
    question_number = 600851475143
    i = int(sqrt(question_number))
    #luckily, we only need to calculate from its square root downwards.
    prime_list = prime.primeList(i)
    prime_list.reverse()
    for x in prime_list:
        #Check if question_number is divisible by a series of primes
        #the first one (largest) we find should be our answer
        if question_number % x == 0:
            return x
    return 0

def eulerchallenge4():
    #highest palindrome found
    max_val = 101
    for a in range(100, 999):
        for b in range(a, 999):
            #Calculate products
            x = a * b
            if x > max_val:     
                y = str(x)
                #reverse order of numbers in string
                y = y[::-1]
                y = int(y)
                #check if higher number is a palindrome
                if x == y:
                    max_val = x
    return max_val

def eulerchallenge5():
    #To check all modulo's 1~20 for a number, we only need to check 11~20
    #we start at 11 and multiply that till we reach modulo 12==0
    #that will be the new starting multiplier till we reach mudulo 13==0 etc
    multiplier = 11
    testNum = 0
    for i in range(12, 21):
        num = multiplier
        while True:
            testNum = testNum + 1
            if num % i == 0:
                multiplier = num
                break
            num = num + multiplier
    return multiplier

