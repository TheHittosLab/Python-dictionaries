teclado1 = {
    "Categoría": "Teclados",
    "Modelo": "HyperX Alloy FPS Pro",
    "Precio": "89,99"
    }

teclado2 = {
    "Categoría": "Teclados",
    "Modelo": "Corsair K55 RGB",
    "Precio": "59,99"
    }

consulta = teclado1["Modelo"], teclado1["Precio"], teclado2["Modelo"], teclado2["Precio"]
print(consulta)

muestraTeclado = dict(teclado1)
print(muestraTeclado)