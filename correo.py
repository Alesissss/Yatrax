from flask_mail import Message

def enviar_correo(datos):
    # Aquí importamos la instancia de Mail dentro de la función,
    # en lugar de hacerlo al nivel de módulo, para evitar importaciones circulares.
    from app import mail

    msg = Message(
        subject=datos.get('asunto', 'Sin asunto'),
        sender=datos['remitente'],
        recipients=[datos['destinatario']],
        body=datos['mensaje']
    )
    mail.send(msg)
