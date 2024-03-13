#!/usr/bin/python3

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def primes_up_to_n(n):
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes

def optimal_move(nums):
    # If there are no prime numbers left, return -1
    if not any(is_prime(num) for num in nums):
        return -1
    # If there's only one prime number, return its index
    if nums.count(1) == 1:
        return nums.index(1)
    # Otherwise, return the index of the first prime number
    for i, num in enumerate(nums):
        if is_prime(num):
            return i

def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        primes = primes_up_to_n(n)
        moves = 0
        while True:
            index = optimal_move(primes)
            if index == -1 or moves % 2 == 0:
                if moves % 2 == 0:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break
            else:
                move = primes[index]
                primes = [p for p in primes if p % move != 0]
                moves += 1
    if maria_wins == ben_wins:
        return None
    return "Maria" if maria_wins > ben_wins else "Ben"
