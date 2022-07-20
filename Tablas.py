
"""CODIGO QUE ACEPTA NUMEROS FLOTANTES"""

Tabla = float(input("Ingresa un valor entre 1 y 10: "))

while True:


    if Tabla<=10 and Tabla>=1:

        for n in range (0,11):
            Resultado = Tabla*n
            print(("%f x %d = %f") % (Tabla,n,Resultado))
            
        break

    else:
        Tabla = float(input("Ingresa un valor entre 1 y 10: "))
