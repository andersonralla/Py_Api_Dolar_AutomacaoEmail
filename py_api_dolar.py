
import requests

# API

# http://economia.awesomeapi.com.br/json/last/USD-BRL

requisicao = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL")

# print(requisicao)

#print(requisicao.json())

requisicao_dicionario = requisicao.json()

#cotacao = requisicao_dicionario['USDBRL']['bid']

cotacao = float(requisicao_dicionario['USDBRL']['bid'])

print(cotacao)


# ENVIO EMAIL

import smtplib
import email.message

def enviar_email(cotacao):
    corpo_email = f"""
    <p>Dólar está abaixo de R$5.25. Cotação atual: R${cotacao}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Dólar está abaixo do valor R$5.25"
    msg['From'] = '@gmail.com'
    msg['To'] = '@gmail.com'
    password = 'password'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

if cotacao < 5.25:
    enviar_email(cotacao)




#deploy

# heroku login

# git init

# heroku git:remote -a pyalertastudyapi

# pip freeze > requirements.txt

# git add .
# git commit -am "Uppp"
# git push heroku master

#HEROKU pyalertastudyapi

