N, K, M = map(int, input().split())
if M >= K:
    way1 = abs(M - K)
    print(way1 - 1)
elif K > M:
    way1 = (N - K + M)
    print(way1 - 1)
else:
    way2 = (N - M + K)
    print(way2 - 1)
