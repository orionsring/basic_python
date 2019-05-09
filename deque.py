# sample file to practice using the python library
# specifically the function deque(), pronounced "Deck"
# recommended to use these lines of code in a python repl.

from collections import deque

deck = deque([2,3,5,7,11,17,19])

[m for m in dir(list) if not m.startswith('__')]
# ['append', 'count', 'extend', 'index', 'insert', 'pop',\
# 'remove', 'reverse', 'sort']

[m for m in dir(deque) if not m.startswith('__')=]
# ['append', 'appendleft', 'clear', 'copy', 'count', \
# 'extend', 'extendleft', 'index', 'index', 'insert', \
# 'maxlen', 'pop', 'popleft', 'remove', 'reverse', 'rotate']


deck2 = deque(maxlen=5)

deck2.extend(range(5))
deck2
# deque([0, 1, 2, 3, 4])

deck2.append(10)
deck2
# deque([1, 2, 3, 4, 10])

deck2.appendleft(0)
deck2
# deque([0, 1, 2, 3, 4])

primes = [2,3,5,7,11,13,17,19]
prime_deck = deque(primes)
prime_deck
# deque([2, 3, 5, 7, 11, 13, 17, 19])

prime_deck.rotate(4)
prime_deck
# deque([11, 13, 17, 19, 2, 3, 5, 7])

prime_deck.rotate(-2)
prime_deck
# deque([17, 19, 2, 3, 5, 7, 11, 13])

prime_deck.rotate(20)
prime_deck
# deque([5, 7, 11, 13, 17, 19, 2, 3])

for x in range(5):
    prime_deck.rotate(x * len(prime_deck))
    print(prime_deck)
# deque([5, 7, 11, 13, 17, 19, 2, 3])
# deque([5, 7, 11, 13, 17, 19, 2, 3])
# deque([5, 7, 11, 13, 17, 19, 2, 3])
# deque([5, 7, 11, 13, 17, 19, 2, 3])
