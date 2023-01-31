"""
    Programa6
    Nombre: Kevin AC
    Fecha:31/01/2023
    Descripcion:Area y perimetro del circulo y cuadrado.
"""
print("Area y perimetro del circulo") #un print para que se de un espacio de una linea
print("Area del circulo")
radio=int(input("Radio: "))
PI=3.1416
perimetro_cir=2*radio*PI
area_cir=PI*radio**2
print("El perimero del circulo es: ", perimetro_cir)
print("El area del circulo es: ", area_cir)
lado=int(input("medida del lado: "))
perimetro_cua= lado*4
area_cua= lado*lado
print("El perimetro del cuadrado: ", perimetro_cua)
print("El area del cuadrado:", area_cua)
