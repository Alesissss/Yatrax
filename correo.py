from flask_mail import Message

def enviar_correo(mail, datos):
    # mail es el argumento que recibe la función
    msg = Message(
        subject=datos.get('asunto', 'Sin asunto'),
        sender=datos['remitente'],
        recipients=[datos['destinatario']],
        body=datos['mensaje']
    )
    mail.send(msg)  # ¡Aquí mail existe porque es un argumento!
