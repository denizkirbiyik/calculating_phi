import decimal;

iter = int(input("How many iterations of the Fibbonaci sequence should be calculated? : "))
decimal.getcontext().prec = 1+(int(input("How many digits would you like to display? : ")));
n = 1; o = 1; p = 1;

for i in range(iter):
    p = o
    o = n+o
    n = p
    phi = decimal.Decimal(o)/decimal.Decimal(n)
print(phi)
