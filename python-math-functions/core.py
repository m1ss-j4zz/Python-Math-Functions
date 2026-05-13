# Factorial - fac(n)
def fac(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return n * (fac(n - 1))

# Fibonnaci - fib(n)
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        n1, n2 = 0, 1
        for num in range(2, n + 1):
            n1, n2 = n2, n1 + n2
        return n2
    
# Triangular Number - tri(n)
def tri(n):
    n1 = n + 1
    n2 = n * n1
    return n2 // 2
    
# Exponate - exp(n)
def exp(n, e):
    return n ** e

# Collatz Sequence - cc(n)
def cc(n):
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n) + 1
        steps += 1
    return steps

# Even or Odd - eo(n)
def eo(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# Greatest Common Diviser - gcd(n, b)
def gcd(n, b):
    n, b = abs(n), abs(b)
    while b > 0:
        n, b = b, n % b
    return n

# Least Common Multiple - lcm(n, b)
def lcm(n, b):
    top = abs(n * b)
    bottom = gcd(n, b)
    return top // bottom

# Comprime? - copm(n, p)
def copm(n, b):
    if gcd(n, b) == 1:
        return True
    else:
        return False
    
# N Choose R - ncr(n, b)
def ncr(n, b):
    top = fac(n)
    bottom = fac(b) * fac((n - b))
    return top // bottom

# Area of Rectangle - ar(b, h)
def ar(b, h):
    return b * h

# Area of Triangle - at(b, h)
def at(b, h):
    return 0.5 * b * h

# Area of Circle - ac(r)
def ac(r):
    return 0.5 * r * 3.141592653589793

# Nth Term - nthgeo(x, y, n) and nthari(x, y, n)
def nthgeo(x, y, n):
    r = y / x
    return x * (r ** (n - 1))

def nthari(x, y, n):
    d = y - x
    return x + d * (n - 1)

# Sum of Geometric Sequence - sumgeo(x, y, z) and sumgeoN(x, y, z, n)
def sumgeo(x, y, z):
    if y // x == z // y:
        r = y / x
        if abs(r) < 1:
            return x / (1 - r)
        else:
            return "series diverges"
    else:
        return "not a geometric sequence"
    
def sumgeoN(x, y, z, n):
    if y // x == z // y:
        r = y / x
        return x * ((1 - r ** n) / 1 - r)
    else:
        return "not a geometric sequence"
    
# Sum of Arithmetic Sequence - sumariN(x, y, z, n)
def sumariN(x, y, z, n):
    if abs((z - y) - (y - x)) <= 0.0000000001:
        return (n / 2) * (x + nthari(x, y, n))
    else:
        return "not an arithmetic sequence"
