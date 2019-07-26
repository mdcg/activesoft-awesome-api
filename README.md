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

```
Saida do Django
```

## Ações

### Cadastrar um usuário:

```shell
curl --location --request POST "localhost:8000/api/v1/signup" \
  --form "email=mauro@python.com" \
  --form "username=mdcg" \
  --form "password=123456" \
  --form "first_name=Mauro"
```

### Login

```shell
curl --location --request POST "localhost:8000/api/v1/signin" \
  --form "username=mdcg" \
  --form "password=123456" \
```

## Misc

### Acessando um container no Docker

Se você precisar acessar o container do aplicativo, para executar manualmente alguma migração ou qualquer coisa, use os seguintes comandos:

```
$ docker ps
```

Depois de executar este comando, você terá acesso ao ID (uma sequência hexadecimal exibida na primeira coluna) e ao nome do container (exibido na coluna final). Copie um dos dois e execute o seguinte comando:

```
$ docker exec -it <nome ou id_do_container> bash
```

### Debugging

Se você precisar depurar o aplicativo, antes de adicionar 'pdb' ao seu código, execute o seguinte comando:

```
$ docker attach <nome ou id_do_container>
```

Se você não souber como acessar o nome ou o ID do container, vá para "Acessando um container no Docker".