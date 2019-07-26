# activesoft-awesome-api

[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/mdcg/activesoft-awesome-api/blob/master/LICENSE)

## Introdução

Antes de mais nada, muito obrigado pela oportunidade de mostrar um pouco do meu trabalho. A seguir irei falar um pouco sobre as tecnologias que utilizei para a elaboração deste desafio:

- Docker;
- Docker Compose;
- Django;
- PostgreSQL;

Por que usar o Docker? Porque, o Docker é uma ferramenta projetada para facilitar a criação, implantação e execução de aplicativos usando containers. Os containers permitem que um desenvolvedor empacote um aplicativo com todas as partes de que precisa, como bibliotecas e outras dependências, e envie tudo como um único pacote. Ao fazer isso, graças ao container, o desenvolvedor pode ter certeza de que o aplicativo será executado em qualquer outra máquina Linux independentemente de quaisquer configurações personalizadas que a máquina possa ter e que possam diferir da máquina usada para gravar e testar o código.

O aplicativo inteiro já está configurado para ser executado no container do Docker. Por esse motivo, sugiro que você tenha o Docker e o Docker Compose instalados em sua máquina.

Para instalá-los, basta clicar nos links abaixo:

- [Install Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

## Primeiros passos

Na pasta raiz do projeto, onde os arquivos `Dockerfile` e `docker-compose.yml` estão localizados, execute o seguinte comando:

```shell
$ docker-compose up
```

***PS: Lembre-se de que, para muitos comandos do Docker e do Docker Compose, você precisa conceder privilégios de 'sudo'. Se o comando acima não funcionar, adicione 'sudo' e tente novamente.***

Deve demorar um pouco para a construção do container, então tenha um pouco de paciência. Se tudo correr bem, você verá uma resposta em seu terminal assim:

```shell
Starting activesoft-awesome-api_db_1 ... done
Starting activesoft-awesome-api_web_1 ... done
Attaching to activesoft-awesome-api_db_1, activesoft-awesome-api_web_1
web_1  | Python 3.6.5
db_1   | 2019-07-26 19:03:28.679 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
db_1   | 2019-07-26 19:03:28.679 UTC [1] LOG:  listening on IPv6 address "::", port 5432
db_1   | 2019-07-26 19:03:28.704 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
db_1   | 2019-07-26 19:03:28.736 UTC [23] LOG:  database system was shut down at 2019-07-26 19:03:25 UTC
db_1   | 2019-07-26 19:03:28.753 UTC [1] LOG:  database system is ready to accept connections
web_1  | No changes detected
web_1  | No changes detected in app 'api'
web_1  | Operations to perform:
web_1  |   Apply all migrations: admin, auth, authtoken, contenttypes, sessions
web_1  | Running migrations:
web_1  |   Applying contenttypes.0001_initial... OK
web_1  |   Applying auth.0001_initial... OK
web_1  |   Applying admin.0001_initial... OK
web_1  |   Applying admin.0002_logentry_remove_auto_add... OK
web_1  |   Applying admin.0003_logentry_add_action_flag_choices... OK
web_1  |   Applying contenttypes.0002_remove_content_type_name... OK
web_1  |   Applying auth.0002_alter_permission_name_max_length... OK
web_1  |   Applying auth.0003_alter_user_email_max_length... OK
web_1  |   Applying auth.0004_alter_user_username_opts... OK
web_1  |   Applying auth.0005_alter_user_last_login_null... OK
web_1  |   Applying auth.0006_require_contenttypes_0002... OK
web_1  |   Applying auth.0007_alter_validators_add_error_messages... OK
web_1  |   Applying auth.0008_alter_user_username_max_length... OK
web_1  |   Applying auth.0009_alter_user_last_name_max_length... OK
web_1  |   Applying auth.0010_alter_group_name_max_length... OK
web_1  |   Applying auth.0011_update_proxy_permissions... OK
web_1  |   Applying authtoken.0001_initial... OK
web_1  |   Applying authtoken.0002_auto_20160226_1747... OK
web_1  |   Applying sessions.0001_initial... OK
web_1  | Watching for file changes with StatReloader
web_1  | Performing system checks...
web_1  | 
web_1  | System check identified no issues (0 silenced).
web_1  | July 26, 2019 - 19:03:33
web_1  | Django version 2.2.3, using settings 'core.settings'
web_1  | Starting development server at http://0.0.0.0:8000/
web_1  | Quit the server with CONTROL-C.
```

## Ações

### Cadastrar um usuário

```shell
$ curl --location --request POST "localhost:8000/api/v1/signup" \
  --form "email=mauro@python.com" \
  --form "username=mdcg" \
  --form "password=123456" \
  --form "first_name=Mauro"
```

***PS: Os campos 'first_name' e 'email' são opcionais.***

### Login

```shell
$ curl --location --request POST "localhost:8000/api/v1/signin" \
  --form "username=mdcg" \
  --form "password=123456"
```

### Rodando a bateria de testes

Para executar os testes automatizados do projeto, antes de mais nada, você precisa saber como acessar um container no Docker. Caso você não esteja familiarizado, leia o texto da sessão *Misc => Acessando um container no Docker*. Lá terá tudo que você precisa saber para desempenhar essa função.

Após ter aprendido a acessá-lo, você irá executar o seguinte comando na pasta `src/`:

```shell
$ python manage.py test api
```

## Misc

### Acessando um container no Docker

Se você precisar acessar o container do aplicativo, para executar manualmente alguma migração ou qualquer coisa, use os seguintes comandos:

```shell
$ docker ps
```

Depois de executar este comando, você terá acesso ao ID (uma sequência hexadecimal exibida na primeira coluna) e ao nome do container (exibido na coluna final). Copie um dos dois e execute o seguinte comando:

```shell
$ docker exec -it <nome ou id_do_container> bash
```

### Debugging

Se você precisar depurar o aplicativo, antes de adicionar 'pdb' ao seu código, execute o seguinte comando:

```shell
$ docker attach <nome ou id_do_container>
```

Se você não souber como acessar o nome ou o ID do container, vá para "Misc => Acessando um container no Docker".