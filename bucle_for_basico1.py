print("1. Básico:")
for i in range(101):
    print(i)

print("\n2. Múltiplos de 2:")
for i in range(2, 501, 2):
    print(i)

print("\n3. Vanilla Ice:")
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)

print("\n4. Suma de pares (Número gigante):")
suma_total = 0
for i in range(0, 500001, 2):
    suma_total += i
print(suma_total)

print("\n5. Cuenta regresiva de 3 en 3:")
for i in range(2024, 0, -3):
    print(i)

print("\n6. Contador dinámico:")
numInicial = 3
numFinal = 10
multiplo = 2

for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)
        
            