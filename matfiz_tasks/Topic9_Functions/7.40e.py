def function(*args):
    number = len(args)
    if number % 2 != 0:
        print("Impossible!")
        return
    result = 0
    for i in range(number // 2):
        result += (args[i]**2 + args[number//2 + i]**2 + args[i]*args[number//2 + i])
    return result


print(function(1,2,3,4,5,6))
