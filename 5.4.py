number = int(input())
if number // 10 == 1:
    print(number, "попугаев")
else:
    last = number % 10
    if last == 1:
        print(number, "попугай")
    elif 2 <= last <= 4:
        print(number, "попугая")
    else:
        print(number, "попугаев")