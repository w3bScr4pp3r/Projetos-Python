import smtplib
import email.message

server = smtplib.SMTP('smtp.gmail.com:587')  

corpo_email = f"""
<p>Olá,</p>
<p>Este é um teste de e-mail, favor confirmar o recebimento.</p>
<p>At.te,</p>
<p>Daniel Moura Alves</p>
"""

msg = email.message.Message()
msg['Subject'] = "assunto_do_email"

# Fazer antes (apenas na 1ª vez): Ativar Aplicativos não Seguros.
# Gerenciar Conta Google -> Segurança -> Aplicativos não Seguros -> Habilitar
# Caso mesmo assim dê o erro: smtplib.SMTPAuthenticationError: (534,
# Você faz o login no seu e-mail e depois entra em: https://accounts.google.com/printUnlockCaptcha

msg['From'] = 'seu_email'
msg['To'] = 'email_do_destinatario'
password = 'sua_senha'
msg.add_header('Content-Type', 'text/html')
msg.set_payload(corpo_email)

s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()
# Login Credentials for sending the mail
s.login(msg['From'], password)
s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

print('Email enviado')
