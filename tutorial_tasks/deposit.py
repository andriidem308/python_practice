"""
Пользователь делает вклад в размере < m > рублей сроком на < y > лет под 10% годовых
(каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются
к сумме вклада, и на них в следующем году тоже будут проценты).

Написать функцию < bank >, принимающая аргументы < a >  и < y >,
и возвращающую сумму, которая будет на счету пользователя.
"""


def bank(m: float, y: int):
    """
    :param m: money will be invested (float)
    :param y: years will be money on deposit (int)
    :return:  result -> money will be accumulated (float)
    """
    return m * 1.1 ** y


money = float(input("How much money in USD will be invested? Money: "))
years = int(input("How many years the money will be on deposit? Years: "))

result = bank(money, years)
profit = result - money
print("\nMoney will be accumulated:", round(result, 2),
      "USD in", years, "years from", money, "USD.\nProfit:", round(profit, 2), "USD.")
