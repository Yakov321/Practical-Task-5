knats = int(input())

sickles = knats // 29
galleon = sickles // 17
sickle = sickles % 17
knat = knats % 29

if galleon > 0:
    print (f"{galleon} галлеонов ")
if sickle > 0:
    print(f"{sickle} сиклей ")
if knat > 0:
    print(f"{knat} кнатов")
