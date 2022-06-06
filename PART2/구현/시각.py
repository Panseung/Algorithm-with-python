# p.113 시각

N = int(input())
cnt = 0
res_h, res_m, res_s = 0, 0, 1

while res_h <= N:
    if '3' in str(res_h) or '3' in str(res_m) or '3' in str(res_s):
        cnt += 1

    res_s += 1
    if res_s == 60:
        res_m += 1
        res_s = 0
    if res_m == 60:
        res_h += 1
        res_m = 0

print(cnt)
