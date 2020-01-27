"""
You are given all numbers between 1,2,…,n except one. Your task is to find the missing number.

Input
The first input line contains an integer n.
The second line contains n−1 numbers. Each number is distinct and between 1 and n (inclusive).

Output
Print the missing number.
"""

n = int(input())
nums = list(map(int, input().split()))

initial_sum = ((1 + n)*n) // 2
curr_sum = sum(nums)

print(initial_sum - curr_sum)
