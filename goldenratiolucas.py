import decimal;
decimal.getcontext().prec = 10**4

iter = int(input("How many iterations of the Fibbonaci sequence should be calculated? : "))
n = 2; o = 1; p = 1;

for i in range(iter):
    p = o
    o = n+o
    n = p
    phi = decimal.Decimal(o)/decimal.Decimal(n)
print(phi)