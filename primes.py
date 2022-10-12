"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

def primes(number_of_primes):
    list = []
    numerator = 1
    while len(list) < number_of_primes:
        numerator = numerator+1
        for denominator in range (2,numerator):
            if (numerator%denominator == 0):
                break
        else:
            list.append(numerator)

    return list
