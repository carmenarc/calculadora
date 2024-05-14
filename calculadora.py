x = 5 
y = 10
print(x + y)  # y no ha sido definido previamente
def funcion():
    return 5

print("Este código nunca se ejecutará después del retorno.") 
def suma(a, b):
    return a + b

# Llamamos a la función con algunos valores
resultado = suma(3, 4)
print("El resultado de la suma es:", resultado)
for i in range(5):
    print(i)
    if i == 2:
        print("Customer Success")
        break  # Salimos del bucle cuando i es igual a 2
print("Fin del bucle")
def multiplicar(a, b):
    try:
        return a * int(b)  # Intenta convertir b a un entero antes de la multiplicación
    except ValueError:
        return "Error: El segundo argumento no es un número"

# Llamada a la función con parámetros de tipo diferente 
resultado = multiplicar(3, "4")
print("El resultado de la multiplicación es:", resultado)
 # Uso de un puntero sin haber sido asignado previamente 
puntero = None 
print(puntero) 