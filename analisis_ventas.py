# 1. Carga de Datos
ventas = [
    {"fecha": "2024-01-01", "producto": "Laptop", "cantidad": 2, "precio": 1200.0},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 25.0},
    {"fecha": "2024-01-02", "producto": "Laptop", "cantidad": 1, "precio": 1200.0},
    {"fecha": "2024-01-02", "producto": "Teclado", "cantidad": 3, "precio": 45.0},
    {"fecha": "2024-01-03", "producto": "Mouse", "cantidad": 2, "precio": 25.0}
]

# 2. Cálculo de Ingresos Totales
ingresos_totales_global = 0
for venta in ventas:
    ingresos_totales_global += venta["cantidad"] * venta["precio"]

# 3. Análisis del Producto Más Vendido
ventas_por_producto = {}
for venta in ventas:
    prod = venta["producto"]
    cant = venta["cantidad"]
    if prod not in ventas_por_producto:
        ventas_por_producto[prod] = 0
    ventas_por_producto[prod] += cant

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)

# 4. Promedio de Precio por Producto (Usando Tuplas)
precios_por_producto = {}
for venta in ventas:
    prod = venta["producto"]
    precio_total_venta = venta["precio"] * venta["cantidad"]
    cantidad_venta = venta["cantidad"]
    
    if prod not in precios_por_producto:
        precios_por_producto[prod] = (0, 0) # (suma_precios, cantidad_total)
    
    actual_suma, actual_cant = precios_por_producto[prod]
    precios_por_producto[prod] = (actual_suma + precio_total_venta, actual_cant + cantidad_venta)

# 5. Ventas por Día
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    if fecha not in ingresos_por_dia:
        ingresos_por_dia[fecha] = 0
    ingresos_por_dia[fecha] += ingreso

# 6. Representación de Datos (Resumen Ventas)
resumen_ventas = {}
for prod, datos in precios_por_producto.items():
    suma_ingresos, cant_total = datos
    resumen_ventas[prod] = {
        "cantidad_total": cant_total,
        "ingresos_totales": suma_ingresos,
        "precio_promedio": suma_ingresos / cant_total
    }

# --- IMPRESIÓN DE RESULTADOS PARA LA ENTREGA ---
print(f"1. LISTA DE VENTAS ORIGINAL:\n{ventas}")
print(f"\n2. INGRESOS TOTALES GENERADOS: ${ingresos_totales_global}")
print(f"\n3. PRODUCTO MÁS VENDIDO: {producto_mas_vendido} ({ventas_por_producto[producto_mas_vendido]} unidades)")
print("\n4. PRECIO PROMEDIO POR PRODUCTO:")
for prod, info in resumen_ventas.items():
    print(f"   - {prod}: ${info['precio_promedio']:.2 f}")
print(f"\n5. INGRESOS TOTALES POR DÍA: {ingresos_por_dia}")
print(f"\n6. RESUMEN DE VENTAS POR PRODUCTO: {resumen_ventas}")