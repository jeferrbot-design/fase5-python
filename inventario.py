# Programa de inventario y reabastecimiento
inventario = [
    ["A01", "Teclado", 3, 10],
    ["A02", "Mouse", 15, 10],
    ["A03", "Monitor", 2, 5],
    ["A04", "Impresora", 8, 8],
    ["A05", "Parlantes", 1, 4]
]
def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0

    return cantidad

print("INFORME DE REABASTECIMIENTO")

for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    pedido = calcular_pedido(stock_actual, stock_minimo)

    print("Código:", codigo)
    print("Artículo:", nombre)
    print("Stock actual:", stock_actual)
    print("Stock mínimo:", stock_minimo)
    print("Cantidad a pedir:", pedido)
    print("------------------------------")
