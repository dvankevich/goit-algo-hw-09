import timeit

coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
  result = {}
  for coin in coins:
    if amount >= coin:
      result[coin] = amount // coin # визначає, скільки монет певного номіналу можна використати
      amount %= coin # оновлює залишок суми, яка ще має бути зібрана
  return result


def find_min_coins(amount):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0

    used_coins = [0] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if min_coins[x - coin] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - coin] + 1
                used_coins[x] = coin

    result = {}
    while amount > 0:
        coin = used_coins[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


assert find_coins_greedy(113) == {1: 1, 2: 1, 10: 1, 50: 2}
assert find_min_coins(113) == {1: 1, 2: 1, 10: 1, 50: 2}

amounts = [8, 17, 39, 61, 128, 250, 500, 1008, 2049, 4096]
results = []

for amount in amounts:
    print(amount)
    print(find_coins_greedy(amount))
    print(find_min_coins(amount))
    time_greedy = timeit.timeit(lambda: find_coins_greedy(amount), number=1000)
    time_dp = timeit.timeit(lambda: find_min_coins(amount), number=1000)
    results.append([amount, time_greedy, time_dp])

print(f"{'Amount':>8} | {'greedy (s)':>14} | {'DP (s)':>14}")
for result in results:
    print(f"{result[0]:>8} | {result[1]:>14.8f} | {result[2]:>14.8f}")