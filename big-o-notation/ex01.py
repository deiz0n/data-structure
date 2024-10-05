import timeit

# notation: 0(n) -> 0(11)
def soma1(n):
    soma = 0
    for i in range(n+1):
        soma += i
    return soma

# notation: 0(3)
def soma2(n):
    return (n * (n + 1)) / 2

time1 = timeit.timeit(lambda: soma1(10), number=1000)
time2 = timeit.timeit(lambda: soma2(10), number=1000)

print(f"Tempo de execução da primeira função: {time1:.6f}")
print(f"Tempo de execução da segunda função: {time2:.6f}")