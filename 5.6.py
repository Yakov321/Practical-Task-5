day1 = int(input())
day2 = int(input())
day3 = int(input())

if day1 == day2 and day1 == day3:
    print('3')
elif day1 == day2 or day1 == day3 or day2 == day3:
    print('2')
else:
    print('1')
