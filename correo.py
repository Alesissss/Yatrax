from flask_mail import Message
import os

def enviar_correo(mail_instancia, datos):
    try:
        msg = Message(
            subject=datos['asunto'],
            sender=datos['remitente'],
            recipients=[datos['destinatario']],
            body=datos['mensaje']
        )

        # Si se especifica un archivo para adjuntar
        if 'archivo_adjunto' in datos and datos['archivo_adjunto']:
            archivo_path = datos['archivo_adjunto']
            if os.path.exists(archivo_path):
                with open(archivo_path, 'rb') as archivo:
                    archivo_nombre = os.path.basename(archivo_path)
                    msg.attach(
                        filename=archivo_nombre,
                        content_type='application/pdf',
                        data=archivo.read()
                    )
                print(f"[INFO] Archivo adjunto: {archivo_nombre}")
            else:
                print(f"[WARNING] Archivo no encontrado: {archivo_path}")

        mail_instancia.send(msg)
        print(f"[INFO] Correo enviado exitosamente a {datos['destinatario']}")
    except Exception as e:
        print(f"[ERROR enviar_correo] {e}")
