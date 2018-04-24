"""
https://pl.python.org/docs/whatsnew/section-generators.html
"""
def wygeneruj_calkowite(N):
    for i in range(N):
        yield i

gen = wygeneruj_calkowite(3)
print(gen)
print(dir(gen))
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())