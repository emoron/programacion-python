#Aracely Velazquez Calderon
#Laboratorio 3
#29/11/2016
#Ejercicio 6

ap=input("ingresa los años-persona: ")
if ap < 1:
    print "error de entrada"
elif ap == 1:
    a=ap*10.5
    print ap, "año-persona equivale a", a, "años-perro"
elif ap == 2:
    b=ap*10.5
    print ap, "años-persona equivale a", b, "años-perro"
elif ap > 2:
    c=ap*4
    print ap, "años-persona equivale a", c, "años-perro"
