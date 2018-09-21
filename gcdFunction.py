def gcd(a,b):
    """
    Returns the greatest common divisor of a and b
    """
    while b > 0:
        a, b = b, a % b

    return a

print(gcd(50,20))
print(gcd(20, 50))  # It does not matter wheter a or b is bigger
print(gcd(22, 143))        
