# config.py

# Configurações do site / aplicativo
APP = {
    # Nome do site para a tag `<title>...</title>`
    'title': 'MyPyPad',

    # Nome / logo do site, em HTML, para a tag `.navbar-brand` e outros usos
    'name': 'My<i class="bi bi-filetype-py text-warning px-0"></i>Pad',

    # Chave secreta (48 caracteres)
    # Obtenha essa chave rodando `python keygen.py`
    'secret_key': 'e4e77e9bb7f88ad9e20a95a0b79b2ce8c6ec75d3cd01d7582ef37faf8a93808fa4eae7d0d6ae879a4f1902f9b21da2c7',
}

# Configurações do banco de dados
DB = {
    'name': 'database.db',
}

# Configurações dos cookies
COOKIE = {
    'livedays': 30,
}

# Configurações do e-mail
MAIL = {
    # Boolean: True envia e-mails, False não envia 
    "send_contact": True,

    # Servidor SMTP e porta do Gmail / provedor
    "server": "smtp.gmail.com",
    "port": 587,

    # Conta de e-mail do administrador do site
    "username": "glaubernascimento890@gmail.com",
    "admin_email": "glaubernascimento890@gmail.com",
    
    # Acesse https://myaccount.google.com/apppasswords para gerar a senha de aplicativo abaixo
    "password": "ggvd puxk qrzc vngz",
}
 