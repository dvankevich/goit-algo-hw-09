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
  pass

amounts = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

assert find_coins_greedy(113) == {1: 1, 2: 1, 10: 1, 50: 2}

