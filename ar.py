from email.message import EmailMessage
import smtplib
import random

# Cuentas
posiblesRemitentes = {"Correo" : "Código de seguridad", #aquí se cambian los correos y contraseñas de aplicación
                      "Correo" : "Código de seguridad"}
# Destinatario y mensaje
destinatario = input("Digite su destinatario: ")

# Función para generar cadena aleatoria
def enviarcorreo():
    # Este for es para la cantidad de mensajes
    for i in range(20): #modificable para la cantidad de mensajes enviados
        # Esto tomará un usuario aleatorio y su respectiva contraseña
        remitente = random.choice(list(posiblesRemitentes))
        contraseña = posiblesRemitentes[remitente]
        # Listas de letras, números y símbolos que usará para hacer el mensaje aleatorio
        letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', '1', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E' ,'F', 'G', 'H',
                'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        simbolos = ['!', '$', '%', '&', '/', '(', ')', '=', '?', '¡', '¿', '#', '{', '+', '{', '}']
        # Acumulador para el mensaje completo
        mensajeCompleto = ""
        # Este for es para la cantidad de caracteres que se tomarán para enviar el correo    
        for j in range(20): #modificable para la longitud del mensaje
            # Elige aleatoriamente letras y las concatena en un string
            letrasRandom = random.sample(letras, random.randint(1,54))
            letrasConcatenadas = "".join(letrasRandom)
            # Elige aleatoriamente números y los concatena en un string
            numerosRandom = random.sample(numeros, random.randint(1,10))
            numerosConcatenados = "".join(numerosRandom)
            # Elige aleatoriamente símbolos y los concatena en un string
            simbolosRandom = random.sample(simbolos, random.randint(1,16))
            simbolosConcatenados = "".join(simbolosRandom)
            # Junta los strings concatenados en un solo string
            mensaje = f"{letrasConcatenadas}{numerosConcatenados}{simbolosConcatenados}"
            # Como repite constantemente este proceso, lo junta todo en una variable para hacer más largo el mensaje
            mensajeCompleto += mensaje
            # Continua para no quedarse atorado
            continue
        # Hace un objeto de email
        email = EmailMessage()
        # Lo configuramos
        email["From"] = remitente
        email["To"] = destinatario
        email["Subject"] = mensajeCompleto
        # Formamos el cuerpo del correo
        email.set_content(mensajeCompleto)
        # Configura el servidor SMTP, se logea y envía el correo
        smtp = smtplib.SMTP_SSL("smtp.gmail.com")
        smtp.login(remitente, contraseña)
        smtp.sendmail(remitente, destinatario, email.as_string())
        smtp.quit()
enviarcorreo()
