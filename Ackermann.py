

def ack(x, y):


    if x == 0:
        ans = y + 1
    elif y == 0:
        ans = ack(x - 1, 1)
    else:
        ans = ack(x - 1, ack(x, y-1))

    return ans

x = int(input("x>>>"))
y = int(input("y>>>"))
print(ack(x, y))





