#encoding: utf-8
import random

    azar = random.randint( 10, 101 )
    print( azar )
    print( "Ingresa un numero entero entre (10-101):" )
    while int(conta) < 5:
        conta = int(conta) + 1
        print( "Intento No:" + str( conta ) )
        num1 = input()
        num1 = int( num1 )
        if num1 >= 10 and num1 <= 101:
            print( "Digita otro numero:" )
            if num1 < azar:
                print( ">El numero debe ser mayor..." )
            if num1 > azar:
                print( ">El numero debe ser menor..." )
            if num1 == azar and conta == 1:

                print( "FELICIDADES, HAS LOGRADO ADIVINAR A LA PRIMERA " )
                break
            if num1 == azar:
                conta = str( conta )
                print( "GANASTE ADIVINASTE EL NUMERO ALEATORIO , EN EL INTENTO NUMERO: " + conta )
                break
            if num1 != azar and conta == 5:
                print( "PERDISTE SE ACABARON TUS 5 INTENTOS" )
        else:
            print( "ERROR:Debe digitar un numero en el rango(10-101)" )

    print( "DESEA JUGAR OTRA VEZ? DIGITE UN: 1:(SI) 2:(N0)" )
    if deci == 1:
    salir = 1
    else:
    print( "ERROR:DIGITE UN NUMERO VALIDO" )
    salir = 3
