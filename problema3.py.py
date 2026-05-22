# ==================================================
# Fase 5 - Evaluación Final
# Problema 3: Auditoría de Inventario
# Estudiante: [WILSON ZAMORA ORTIZ]
# ==================================================

# Función para calcular la cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):

    # Verifica si el stock actual es menor al mínimo
    if stock_actual < stock_minimo:

        # Calcula la diferencia
        cantidad = stock_minimo - stock_actual
        return cantidad

    else:
        # Si hay suficiente stock no se pide nada
        return 0


# Matriz de inventario
# [Código, Nombre, Stock Actual, Stock Mínimo]
inventario = [
    [1, "Cuadernos", 10, 20],
    [2, "Lapices", 30, 25],
    [3, "Borradores", 5, 15],
    [4, "Marcadores", 18, 18],
    [5, "Colores", 7, 12]
]


# Mostrar lista de pedidos
print("================================")
print("       LISTA DE PEDIDOS")
print("================================")

# Recorrer inventario
for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    # Llamado de la función
    cantidad_pedir = calcular_pedido(
        stock_actual,
        stock_minimo
    )

    # Mostrar resultados
    print("Artículo:", nombre)
    print("Cantidad a solicitar:", cantidad_pedir)
    print("--------------------------------")


input("\nPresione Enter para finalizar...")
