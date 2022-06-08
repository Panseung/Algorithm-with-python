# p.197 부품 찾기

import sys

N = int(sys.stdin.readline().rstrip())
item_lst = list(map(int, sys.stdin.readline().rstrip()))

M = int(sys.stdin.readline().rstrip())
order_lst = list(map(int, sys.stdin.readline().rstrip()))

for item in order_lst:
    start = 0
    end = len(item_lst) - 1
    target = item
    while start <= end:
        mid = (start + end) // 2
        if item_lst[mid] == target:
            print('yes', end=' ')
            break
        elif item_lst[mid] > target:  # 찾는 값이 작으면
            end = mid - 1
        else:
            start = mid + 1
    if start > end:
        print('no', end=' ')
