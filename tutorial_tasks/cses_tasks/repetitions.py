"""
You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest
repetition in the sequence. This is a maximum-length substring containing only one type of character.

Input
The only input line contains a string of n characters.

Output
Print one integer: the length of the longest repetition.
"""

line = input()
if not line: print(0)
elif len(line) == 1: print(1)
else:
    max_seq = 1
    letter = ''
    cur_seq = 1
    for i in range(1, len(line)):
        if line[i-1] == line[i]:
            cur_seq += 1
            max_seq = cur_seq-1+1 if cur_seq > max_seq else max_seq-1+1
        else:
            letter = line[i-1]
            cur_seq = 1
    print(max_seq, letter)

