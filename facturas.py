from fpdf import FPDF 
import string
import random
from datetime import datetime 
import qrcode

nombrePersona=input("ingrese Nombre: ")
numeroPersona=input("ingrese Numero: ")
direcionPersona=input("ingrese Direcion: ")
metodoPersona=input("ingrese Metodo de pago: ")
now = datetime.now()


leters=(''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(3)))

numbers=(''.join(random.SystemRandom().choice(string.digits) for _ in range(2)))
key=f"{leters}{numbers}"
pdf = FPDF() 
total=0
pdf.add_page() 
now = datetime.now()


cordenatey=140 
# create a cell
pdf.image("img.png",x = 0, y=0 , w = 210, h = 297)
pdf.image("THea.jpg",x = 18, y=20 , w = 49.6, h = 21.15)

pdf.set_font("Arial", size = 12) 

pdf.text(x=160, y=20, txt = f"{now.day}/{now.month}/{now.year}",)
precios=[]
pdf.set_font("Arial", size = 30) 

pdf.text(x=85, y=50, txt = "Factura",)
pdf.set_font("Arial", size = 20) 
pdf.text(x=93, y=57, txt = key) 
pdf.text(x=30, y=75, txt = "Nombre:",)
pdf.text(x=120, y=75, txt = "Numero:",)
pdf.text(x=30, y=100, txt = "Direcion:",)
pdf.text(x=120, y=100, txt = "Metodo de pago:",)

pdf.image("box.jpg",x = 30, y=76 , w = 77, h = 15)
pdf.image("box.jpg",x = 30, y=101 , w = 77, h = 15)
pdf.image("box.jpg",x = 120, y=76 , w = 70, h = 15)
pdf.image("box.jpg",x = 120, y=102 , w = 70, h = 15)

pdf.set_font("Arial", size = 13) 

pdf.text(x=33, y=84, txt = nombrePersona,)
pdf.text(x=33, y=109, txt = direcionPersona,)
pdf.text(x=125, y=84, txt = numeroPersona,)
pdf.text(x=125, y=110, txt = metodoPersona.upper(),)

pdf.set_font("Arial", size = 17) 
pdf.text(x=33, y=130, txt = "Producto",)
pdf.text(x=110, y=130, txt = "cantidad",)
pdf.text(x=150, y=130, txt = "valor",)
pdf.line(30, 133, 165, 133)

pdf.set_font("Arial", size = 15) 
while True:
    nombre=input("nombre del producto: ")
    cantidad=input("ingrese la cantidad: ")
    valor=input("ingrese el valor unitario: ")
    precios.append(int(valor)*int(cantidad))
    pdf.text(x=30, y=cordenatey, txt = f"> {nombre}",)
    pdf.text(x=112, y=cordenatey, txt = f"x{cantidad}",)
    pdf.text(x=150, y=cordenatey, txt = f"${valor}",)
    bolean=input("1)Agregar producto \n 2)Generar factura \n :")
    
    if bolean == "2":
        break
    cordenatey+=7
for i in precios:
    total+=i
pdf.line(30, cordenatey+3, 165, cordenatey+3)
pdf.text(x=112, y=cordenatey+9, txt = f"Total :",)
pdf.text(x=150, y=cordenatey+9, txt = f"${total}",)

img = qrcode.make("www.pornhub.com")
f = open("output.png", "wb")
img.save(f)
f.close()

pdf.image("output.png",x = 80,y=cordenatey+13 , w = 50, h = 50)
#pdf.output("da.pdf")
pdf.output(f"{key}-{now.day}#{now.month}#{now.year}.pdf")
print(f"factura creada exitosamente \n {key}-{now.day}#{now.month}#{now.year}.pdf")


