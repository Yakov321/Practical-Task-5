pin = input()
check = list(pin)
pin = int(pin)
if 0 < pin // 1000 < 10 and check[0] != check[1] != check[2] != check[3] and (pin < 1900 or pin > 2050):
    print('OK')
else:
    print('ERROR')
