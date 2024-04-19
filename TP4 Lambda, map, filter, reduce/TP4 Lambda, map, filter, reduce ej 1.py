# Crear funciones lambda que resuelvan las siguientes problemáticas:
# a. Calcule la superficie de un rectángulo
# b. Determine si una nota está aprobada o no (mayor o igual que 4 aprueba). Retorna True por aprobado; False por desaprobado.
# c. Que dado un número invierta su signo (de positivo a negativo y viceversa)
# d. Que dado un nombre determine si su longitud es larga (mayor de 10 caracteres). Retorna True o False.
# e. Dado un valor numérico retorne True si es positivo o cero; False en caso contrario.
# f. Escribe una función que tome dos argumentos: a y b y devuelva la multiplicación de ellos.
# g. Que compare dos valores y retorne True si el primer argumento es mayor que el segundo


superficie = lambda base,altura : base * 2 + altura * 2
print("a. Superficie: ", superficie(10,5))

nota = lambda numero : numero >= 4 
print("b. Aprobado: ", nota(5))

num = lambda numero : - numero if numero <= 0 else - numero
n = -5
print("c.",n,":", num(n))

nombre = lambda nombre : True if len(nombre) > 10 else False
nom = "Alejandro"
print("d.",nom,":",nombre(nom))

num = lambda numero : True if numero >= 0 else False
n = 10
print("e.",n,":",num(n))

num = lambda a,b : a*b
a = 7
b = 8
print("f.",a,"x",b,":",num(a,b))

comparacion = lambda v1,v2 : True if v1 > v2 else False
valor1 = 3
valor2 = 2
print("g. /// Valor 1 ->",valor1,"/// Valor 2 ->",valor2,"/// :",comparacion(valor1,valor2))




    
