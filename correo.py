from flask_mail import Message

def enviar_correo(mail_instancia,datos):
    try:
        msg = Message(
            subject=datos['asunto'],
            sender = datos['remitente'],
            recipients = [datos['destinatario']],
            body = datos['mensaje']
        )

        mail_instancia.send(msg)
    except Exception as e:
        print(f"[ERROR enviar_correo] {e}")
