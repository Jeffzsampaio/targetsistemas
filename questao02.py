n = int(input("Número que quer encontrar: "))
seq = []

def Fib(n):
    a, b = 0, 1
    while a<= n:  
        a, b = b, a + b
        seq.append(a)
    return a

Fib(n)

if n in seq:
    print("Pertence à sequência")
else:
    print("Não pertence à sequência")

print(f"Sequência de Fibonacci gerada: {seq}")
