a = input()
b = input()
az = 0
bz = 0
n = len(a)
for i in range(n):
    if a[i] == '1':
        az += 2**(n-i-1)
m = len(b)
for i in range(m):
    if b[i] == '1':
        bz += 2**(m-i-1)
c = az + bz
