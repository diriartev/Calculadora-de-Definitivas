#Programa para calcular las definitivas de cualquier materia de la U teniendo en cuenta que son solo 3 parciales (3 cortes)
#Dev: Iri21
#Github: https://github.com/Iri-21

print('¡Hola! Con este programa vamos a ver cuál es tu definitiva en la asignatura que desees, teniendo en cuenta que solo serán 3 cortes (de una sola nota cada uno), por favor introduce los datos que te pediremos a cotinucación \n')

Materia = (input('Nombre de la materia: '))

print("\n")

Porcentaje1 = int(input('Por favor introduce el porcentaje que vale el parcial del primer corte (No pongas el signo %): '))
Porcentaje1 = Porcentaje1 / 100

Porcentaje2 = int(input('Por favor introduce el porcentaje que vale el parcial del segundo corte (No pongas el signo %): '))
Porcentaje2 = Porcentaje2 / 100

Porcentaje3 = int(input('Por favor introduce el porcentaje que vale el parcial del tercer corte (No pongas el signo %): '))
Porcentaje3 = Porcentaje3 / 100

print("\n")

while Porcentaje1 + Porcentaje2 + Porcentaje3 == 1:

    Nota1 = float(str(input(f'Por favor pon la nota de tu parcial del primer corte ({int(Porcentaje1 * 100)}%) a continuacion: ')))
    
    while Nota1 <= 5 and Nota1 >= 0:
        acumulado = round(Nota1 * Porcentaje1, 2)
        print(f'Confirmamos que tu nota en el primer parcial fue {Nota1}, llevas un promedio acumulado de {acumulado}')
        break
    else: 
        print('Ha habido un error, la nota no puede ser mayor que 5 ni menor que 0, por favor introduce la nota correctamente \n')
        Nota1 = float(str(input(f'Por favor pon correctamente la nota de tu parcial del primer corte ({int(Porcentaje1 * 100)}%) a continuacion: ')))
        acumulado = round(Nota1 * Porcentaje1, 2)
        print(f'Confirmamos que tu nota en el primer parcial fue {Nota1}, llevas un promedio acumulado de {acumulado}')

    print("\n")

    Nota2 = float(str(input(f'Por favor pon la nota de tu parcial del segundo corte ({int(Porcentaje2 * 100)}%) a continuacion: ')))

    while Nota2 <= 5 and Nota2 >= 0:
        acumulado = round(acumulado + (Nota2 * Porcentaje2), 2)
        print(f'Confirmamos que tu nota en el segundo parcial fue {Nota2}, llevas un promedio acumulado de {acumulado} \n')
        break
    else:
        print('Ha habido un error, la nota no puede ser mayor que 5 ni menor que 0, por favor introduce la nota correctamente \n')
        Nota2 = float(str(input(f'Por favor pon correctamente la nota de tu parcial del segundo corte ({int(Porcentaje1 * 100)}%) a continuacion: ')))
        acumulado = round(acumulado + (Nota2 * Porcentaje2), 2)
        print(f'Confirmamos que tu nota en el segundo parcial fue {Nota2}, llevas un promedio acumulado de {acumulado} \n')
    
    print("\n")

    Nota3 = float(str(input(f'Por favor pon la nota de tu parcial del tercer corte ({int(Porcentaje3 * 100)}) a continuacion: ')))

    while Nota3 <= 5 and Nota3 >= 0:
        definitiva = round(acumulado + (Nota3 * Porcentaje3), 2)
        print(f'Confirmamos que tu nota en el tercer parcial fue {Nota3} \n')
        break
    else:
        print('Ha habido un error, la nota no peude ser mayor que 5 ni menor que 0, por favor introduce la nota correctamente \n')
        Nota3 = float(str(input(f'Por favor pon correctamente la nota de tu parcial del tercer corte ({int(Porcentaje3 * 100)}%) a continuacion: ')))
        definitiva = round(acumulado + (Nota3 * Porcentaje3), 2)
        print(f'Confirmamos que tu nota en el segundo parcial fue {Nota2}, llevas un promedio acumulado de {acumulado} \n')

    print("\n")

    if definitiva >= 3.0:
        print(f'Felicitaciones, tu definitiva es {definitiva} y has aprobado satisfactoriamente la materia "{Materia}"')
    else:
        print(f'Lo siento, tu definitiva es {definitiva} y has reprobado la materia "{Materia}"')
    break
else: 
    print('Lo sentimos, los porcentajes que indicaste superan o no alcanzan el 100%, por ende, no tienen sentido para calcular el procentaje de la materia. \n Por favor vuelve a ejecutar el programa e introduce correctamente los porcentajes \n')




