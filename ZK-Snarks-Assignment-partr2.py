#ZK Snarks Assignment part 2 , My Twitter : @Elsoonfy,

import random

def pollard_rho_dlog(a, beta, n):
    """
    Pollard's rho algorithm for computing discrete logarithms.

    Args:
    - a: Generator of the cyclic group G of prime order n
    - beta: Element beta in G
    - n: Prime order of the cyclic group G

    Returns:
    - The discrete logarithm x = log_a(beta)
    """
    # Initialize variables
    x, a_val, b_val = 1, 0, 0
    x_prev, a_prev, b_prev = x, a_val, b_val

    while True:
        # Compute new values
        x_next = (x_prev * a) % n
        a_next = (a_prev + 1) % n
        b_next = (b_prev + x_prev) % n

        x_next_next = (x_next * a) % n
        a_next_next = (a_next + 1) % n
        b_next_next = (b_next + x_next) % n

        # Check for collision
        if x_next == x_next_next:
            r = (b_next - b_next_next) % n
            if r == 0:
                return None  # Failure
            else:
                x = (r * pow(a_next_next - a_next, -1, n)) % n
                return x  # Success

        # Update variables
        x_prev, a_prev, b_prev = x_next, a_next, b_next


# Test the implementation
def test_pollard_rho_dlog():
    # Test with random 5-digit integers
    a = 2  # Generator
    n = 101  # Prime order of the cyclic group G
    for _ in range(10):
        beta = random.randint(10000, 99999)
        x_expected = pow(a, beta, n)  # Compute discrete logarithm using modular exponentiation
        x_actual = pollard_rho_dlog(a, beta, n)
        print(f"beta: {beta}, Expected x: {x_expected}, Actual x: {x_actual}")
        assert x_actual == x_expected, "Discrete logarithm computation failed"

test_pollard_rho_dlog()
