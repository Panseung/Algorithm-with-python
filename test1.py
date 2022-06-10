def solution(arr):
    answer = []
    pos = 0
    next = arr[0]
    while pos <= len(arr):
        if pos + 1 < len(arr):
            if arr[pos] == arr[pos + 1]:
                pos += 1
            else:
                pos += 1
                answer.append(next)
                next = arr[pos]
        else:
            answer.append(next)
            break
    return answer


arr = list(map(int, input().split()))
print(solution(arr))
