import qrcode
import os

def generar_codigo_qr(texto, cod_boleta):

    directorio = "Static/qr/"
    nombre_archivo = f"{directorio}{cod_boleta}_qr.png"
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    img = qrcode.make(texto)
    img.save(nombre_archivo)
    return nombre_archivo
