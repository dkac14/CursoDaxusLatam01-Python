from fpdf import FPDF

#Consulamos informacion requerida para el documento
print("-------Presupuesto de Consultoria-------")
proyecto = input("Escriba el nombre del proyecto: ")
horas_estimadas = input("Estime horas estimadas a la dedicacion del proyecto: ")
valor_hora = input("Escriba el valor a cobrar por hora: ")
fecha_entrega = input("Fecha de entrega estimada: ")

presupuesto = int(valor_hora) * int(horas_estimadas)


#Variable para crear el pdf
pdf = FPDF()

#Creamos una pagina
pdf.add_page()
#Configuramos tipografia
pdf.set_font("Times", size = 12)

#Agregamos el contenido consultado para agregarlo al PDF
pdf.text(115, 145, proyecto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, str(presupuesto))

#Generamos el archivo PDF
pdf.output("Presupuesto.pdf")

#Confirmamos a usuario creacion de PDF
print("Consultoría de presupuesto generado con total éxito.")
