import smtplib
from email.mime.text import MIMEText

# Dados de autenticação
username = 'seuemail@gmail.com'
password = 'suasenha'

# Informações do e-mail
para = 'destinatario@exemplo.com'
assunto = 'Assunto do e-mail'
mensagem = 'Conteúdo da mensagem'

# Criando o objeto de e-mail
msg = MIMEText(mensagem)
msg['To'] = para
msg['Subject'] = assunto

# Enviando o e-mail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, password)
server.send_message(msg)
server.quit()

print('E-mail enviado com sucesso')
