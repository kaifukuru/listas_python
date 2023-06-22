def calcular_iva(valor_compra:int):
    IVA=0.19
    valor_iva_producto=valor_compra*IVA
    return valor_iva_producto

def descuento_producto(valor_sin_descuento:int,porcentaje_descuento:int):
    descuento=valor_sin_descuento*(porcentaje_descuento/100)
    valor_final = valor_sin_descuento-descuento
    return valor_final

def calcular_IMC(peso,altura):
    #peso dividido en (altura al cuadrado)
    estado="no calculado"

    IMC=peso/altura**2
    if IMC < 18.5:
        estado="Bajo peso"
    elif IMC >=18.5 and IMC <=24.9:
        estado="Adecuado"
    elif IMC >=25 and IMC <=29.9:
        estado="Sobrepeso"
    elif IMC >=30 and IMC <=34.9:
        estado="Obesidad Grado 1"
    elif IMC >=35 and IMC <=39.9:
        estado="Obsedidad grado 2"
    elif IMC >=40:
        estado="Obesidad grado 3"
    return estado + "IMC=" + str(IMC)