# p.217 1로 만들기

def dp(x, cnt):
    if x == 1:
        if d[1] == -1 or d[1] != -1 and cnt < d[1]:
            d[1] = cnt
        return
    elif x > 1:
        d[X] = cnt
        if x % 5 == 0:
            dp(x / 5, cnt + 1)
        if x % 3 == 0:
            dp(x / 3, cnt + 1)
        if x % 2 == 0:
            dp(x / 2, cnt + 1)
        dp(x - 1, cnt + 1)


X = int(input())

d = [-1] * (X + 1)
dp(X, 0)

print(d[1])
