h = list(map(int, input().split()))
if len(h) > 3:
    print('Ошибка.')
else:
    maxH = max(h)
    minH = min(h)
    middleH = sum(h) - maxH - minH
    print(maxH, middleH, minH)
