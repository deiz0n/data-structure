lista = [1, 2, 3, 4, 5]

# Constant - O(1)
def constant(n):
    print(n[0])
    
constant(lista)

# Linear - (n)
def linear(n):
    for i in n:
        print(i)

linear(lista)

# Quadratic - O(n^2)
def quadratic(n):
    for i in n:
        for j in n:
            print(i, j)
            
quadratic(lista)

# Combination
def combination(n):
    # O(1)
    print(n[0])
    
    # 0(5)
    for i in range(5):
        print('test', 1)
    
    # 0(n)
    for i in n:
        print(i)
    
    # 0(n)
    for i in n:
        print(i)
    
    # 0(3)
    print('Python')
    print('Python')
    print('Python')
    
# = 0(1) + 0(5) + 0(3) + 0(n) + 0(n)
# = 0(9) + 0(n) + 0(n)
# = 0(n)