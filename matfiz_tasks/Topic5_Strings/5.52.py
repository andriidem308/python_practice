ch = input('Char symbol: ')

if ord(ch) in range(ord('A'), ord('Z')): print("Uppercase latin letter")
elif ord(ch) in range(ord('a'), ord('z')): print("Lowercase latin letter")
elif ord(ch) in range(ord('0'), ord('9')): print("Digit 0-9")