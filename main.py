import csv

resumen = {}
transacciones = 0
with open('data/sample_sales.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        #print(row)

        producto = row['producto']
        cantidad = int(row['cantidad'])
        ingresos = float(row['precio'])

        #print(producto)
        if producto not in resumen:
            resumen[producto] = {
                'producto': producto,
                'cantidad': 0,
                'ingresos': 0
            }
        resumen[producto]['cantidad'] += cantidad
        resumen[producto]['ingresos'] += cantidad * ingresos
        transacciones += 1

total_vendido = sum(registro['cantidad'] for registro in resumen.values() )

total_valor = sum(registro['ingresos'] for registro in resumen.values() )

print(f'Numero de transacciones {transacciones}')
print(f'Unidades vendidas {total_vendido}')
print(f'Ingresos totales {total_valor}')

print('Ingresos por producto')
for registro in resumen.values():
    print(registro['producto'], registro['ingresos'])

productoMax = max(resumen.values(),
                  key=lambda registro: registro['ingresos'])

print('Productos con mayores ingresos')
print(f'{productoMax['producto']} {productoMax['ingresos']}')
