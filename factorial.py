def factorial(N):
    if N == 0:
        return 1
    if N < 0 :
        return "inválido, ya que un factorial no puede ser un número negativo."
    else:
        return N * factorial(N-1)
N = int(input("Ingrese el número para calcular su factorial: "))
print(f"El factorial de {N} es {factorial(N)}")