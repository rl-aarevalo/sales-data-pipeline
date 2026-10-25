import csv

resumen = {}
transacciones = 0
with open('data/sample_sales.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        #print(row)

        venta_id = row['venta_id']
        producto = row['producto'].strip()
        if not producto:
            print(f'Producto vacio de la venta No. {venta_id} no valida')
            continue
        try:
          cantidad = int(row['cantidad'])
        except ValueError:
            print(f'La cantidad de la venta No. {venta_id} no es valida')
            continue
        if cantidad < 1:
            print(f'La cantidad de la venta No. {venta_id} es cero o negativo no valida')
            continue

        try:
            precio = float(row['precio'])
        except ValueError:
            print(f'El precio de la venta No. {venta_id} no es valida')
            continue
        if precio < 0:
            print(f'El precio de la venta No. {venta_id} es negativo no valida')
            continue

        #print(producto)
        if producto not in resumen:
            resumen[producto] = {
                'producto': producto,
                'cantidad': 0,
                'ingresos': 0
            }
        resumen[producto]['cantidad'] += cantidad
        resumen[producto]['ingresos'] += cantidad * precio
        transacciones += 1

if len(resumen) < 1:
    print('No se ha encontrado ningun producto')
else:
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
