import qrcode

def generar_codigo_qr(texto, cod_boleta=1111):
    nombre_archivo = f"{cod_boleta}_qr.png"
    img = qrcode.make(texto)
    img.save(nombre_archivo)
    return nombre_archivo