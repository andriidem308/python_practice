while True:
    try: n, m, k = map(int, input().split())
    except: break
    if not (n + m + k): break

    if m % 2: print("Keka")
    else: print("Gared")
