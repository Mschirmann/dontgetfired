# PI_3A


Como instalar e configurar o projeto:
1. Baixe o repositório
2. Abra o repositório em algum editor de código (Visual Code Studio, por exemplo).
4. Dentro da pasta principal pi3a é necessário criar uma venv. Comando abaixo:
5. python3 -m venv venv
6. Ative a venv, no caso do Mac o comando é: source /venv/bin/activate
7. Instale os requirements para executar o projeto com o comando: pip install -r requirements.txt


Para configurar o banco de dados:
1. Instale o mysql de acordo com o seu SO: https://dev.mysql.com/doc/refman/8.0/en/installing.html
2. Após instalar suba o mysql server e crie uma nova Database: CREATE DATABASE pi3a;

Para executar o projeto:
1. Com o Visual Code Studio aberto, abra um novo terminal
2. Veja se a sua venv está ativada (passo 6 da configuração do projeto)
3. Execute o comando: python manage.py migrate
4. Execute o comando: python manage.py runserver
