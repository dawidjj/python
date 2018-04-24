"""
do cache funckji dekorator lru_cache
lru_cache(maxsize=128, typed=False)
jeśli nie ustawimy maxsize to cache może rosnąć do ogromnych rozmiarów
ustawienie typed na true spowoduje, że argumenty różnych typów będą dodawane do cache osobno np. 3 i 3.0 będą traktowane inaczej
fib.cache_info()
fib.cache_clear()
"""

from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print([fib(n) for n in range(10)])
print(fib.cache_info())