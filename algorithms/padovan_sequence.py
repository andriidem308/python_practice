def PadovanElement(n):
    forSwap = [1, 1, 1]
    num = 1
    an = 1
    while an < n:
        an = forSwap[0] + forSwap[1]
        forSwap = [forSwap[1], forSwap[2], an]
        num += 1
    return num, forSwap[1]


def pad(n):
    # 0th ,1st and 2nd number of the series are 1
    pPrevPrev, pPrev, pCurr, pNext = 1, 1, 1, 1

    # Find n'th Padovan number using recursive
    # formula.
    for i in range(3, n + 1):
        pNext = pPrevPrev + pPrev
        pPrevPrev = pPrev
        pPrev = pCurr
        pCurr = pNext

    return pNext;


# Driver Code
print(PadovanElement(100000))
