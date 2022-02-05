n = int(input())
m = int(input())

def ggt(a, b):
    while b!=0:
        a, b = b, a%b
    return a

print(n // ggt(n, m), m // ggt(n, m))
