import timeit

# notation: 0(n) -> 0(1000)
def lista1(n):
    lista = []
    for i in range(1000):
        lista += [i]
    return lista

# notation: 0(1)?
def lista2(n):
    return range(1000)

time1 = timeit.timeit(lambda: lista1(10), number=1000)
time2 = timeit.timeit(lambda: lista2(10), number=1000)

print(f"Tempo de execução da primeira função: {time1:.6f}")
print(f"Tempo de execução da segunda função: {time2:.6f}")