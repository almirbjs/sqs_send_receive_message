# sqs_send_receive_message
Este projeto tem a finalidade de produzir e receber uma mensagem da fila sqs da AWS  

### Ambiente de Desenvolvimento Integrado (IDE) utilizado
PyCharme edição 2022.3.2

## INSTALAÇÃO LOCAL

### Docker

* Execute o arquivo docker compose que esta no diretorio /app deste projeto

### AWS CLI
* baixe e instale pelo link: https://docs.aws.amazon.com/pt_br/cli/latest/userguide/getting-started-install.html

### Fila SQS
* Criar

`aws --endpoint-url=http://localhost:4566 sqs create-queue --queue-name minha-fila-sqs-queue`

* Lê mensagem

`aws --endpoint-url=http://localhost:4566 sqs receive-message --queue-url http://localhost:4576/queue/minha-fila-sqs-queue --max-number-of-messages 10`

## Configuração do projeto python

* Para executar o projeto, primeiro execute o seguinte comando no diretório raiz do projeto
    `pip install -r requirements.txt`




