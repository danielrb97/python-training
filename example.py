import random
from openpyxl import Workbook
import openpyxl
import pycountry

archivo = open("Python24EneroLista.txt")
lista_nombres = []


numero = 1000000
var = 0
for i in archivo:
    var = random.randint(1,numero)
    lista_nombres.append([i.strip("\n"),list(pycountry.countries)[random.randint(1,len(pycountry.countries))].name,var])
    numero = numero - var
    if numero == 0:
        numero = 1



print(lista_nombres[2])

wb = openpyxl.Workbook()
doc = wb.active

doc.append(('Name', 'City', 'Amount'))

for i in lista_nombres:
    doc.append(i)

wb.save("Trabajo_curso.xlsx")


