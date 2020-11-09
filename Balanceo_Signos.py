from pyfiglet import Figlet
import os

os.system('cls') # <=Limpia la consola en windows

desk=Figlet(font='slant')
print (desk.renderText('Signos GH'))  #Banner :)

#Balanceo de signos

signos="[[(]]{})"
cadena = list(signos)

print(f"Analizar signos: {signos}\n")

#parentesis
abre= cadena.count('(')
cierre= cadena.count(')')
#llaves
abre2= cadena.count('[')
cierre2= cadena.count(']')
#corchetes
abre3= cadena.count('{')
cierre3= cadena.count('}')

if abre == cierre and abre2 == cierre2 and abre3 == cierre3:
	print("Balanceo Correcto de Signos =)")

else:
	print("Fall0, falta signo =(")