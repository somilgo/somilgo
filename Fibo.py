
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

x = int(input("Number of digits to go to>>"))
for i in range(0, x+1):
    print(fibo(i))
input('Press ENTER to Exit')