# My Twitter @Elsoonfy, This is Assignment 1 Part1

import random
from math import gcd

def pollard_rho(n):
    """
    Pollard's rho algorithm for factoring integers.
    
    Args:
    - n: Composite integer to be factored
    
    Returns:
    - A non-trivial factor of n
    """
    def f(x):
        return (x * x + 1) % n
    
    # Here i Initialize variables
    a, b = random.randint(2, n-1), random.randint(2, n-1)
    d = 1
    
    # This is the Pollard's rho algorithm
    while d == 1:
        a = f(a)
        b = f(f(b))
        d = gcd(abs(a - b), n)
    
    # Here i Check if a non-trivial factor was found
    if 1 < d < n:
        return d
    else:
        return None  #Then Factorization failed

# Here i Test the implementation
if __name__ == "__main__":
    n = int(input("Enter a composite integer to be factored: "))
    factor = pollard_rho(n)
    if factor:
        print(f"A non-trivial factor of {n} is: {factor}")
    else:
        print("Factorization failed. Try with another number.")
