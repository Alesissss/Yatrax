import qrcode

def generar_codigo_qr(texto, nombre_archivo="codigo_qr.png"):
    img = qrcode.make(texto)
    img.save(nombre_archivo)
    return nombre_archivo