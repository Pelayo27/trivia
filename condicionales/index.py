# Escriba un progna reciba un número e imprima si el valor es positivo o negativo
# Consideral el 0 pisitivo

try:
    number= int(input('Ingrese un número positivo o negativo: '))
    if number>=0:
        print('El número es Positivo')
    else:
        print('El número es negativo')
except:
    print('Valor no definido')

#Escribir un programa reciba un número, se lo multiplique por el mismo#e imprima 
#si el valor resultante es positivo o negativo consider el 0 como positivo
try:
    number= int(input('Ingrese un número positivo o negativo: '))
    newNumber=number*number
    print(newNumber)
    if newNumber>=0:
        print(f"El número {newNumber} es Positivo ")
    else:
        print(f"El número {newNumber} es negativo")
except:
    print('Valor no definido')

# Escriba un programa reciba dos números e imprima el mayor número

try:
    number1= int(input('Ingrese primer número: '))
    number2= int(input('Ingrese segundo número: '))
    if number1>number2:
        print(f"El número mayor es {number1} ")
    elif number2>number1:
        print(f"El número mayor es {number2} ")
    else:
        print(f"Los número son iguales {number2} = {number2}")
except:
    print('Valor no definido')