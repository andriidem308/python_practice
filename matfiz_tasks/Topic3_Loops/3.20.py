n = int(input("Enter n: "))
if n < 0: print("Try again!")
elif n == 0: print("Result = 1")
elif n == 1 or n == 2: print("Result =", 1/3)
else:
    for_swap = [1.0, 1.0, 3.0]
    mult = 1
    for k in range(3, n + 1):
        ak = for_swap[0] + for_swap[1] / 2**for_swap[2]
        mult *= ak / 3**k
        for_swap = [for_swap[1], for_swap[2], ak]
    print(mult)
