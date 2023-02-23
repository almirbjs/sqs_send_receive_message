import json
import logging
import os
import boto3
from self import self


class SQSService:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    def __init__(self):
        if os.environ.get('ENVIRONMENT', 'LOCAL') == "LOCAL":
            logging.info("Inicio do envio da mensagem em localStack...")
            queue_url = "http://localhost:4566/000000000000/minha-fila-sqs-queue"
            self.sqs_client = boto3.client("sqs", endpoint_url=queue_url)
        else:
            self.sqs_client = boto3.client("sqs", region_name="sa-east-1")

    def get_queue_url(self):

        logging.info("Inicia o metodo get_queue_url...")

        response = self.sqs_client.get_queue_url(
            QueueName="minha-fila-sqs-queue",
        )
        logging.info("fim do metodo get_queue_url")
        # exemplo de saida: https://sa-east-1.queue.amazonaws.com/xxxx/minha-fila-sqs-queue
        return response["QueueUrl"]

    def envia_mensagem_sqs(self, payload):
        logging.info("Inicia metodo envia_mensagem_sqs ...")
        try:
            logging.info("Enviado mensagem para o SQS Queue ...")

            response = self.sqs_client.send_message(
                QueueUrl="http://localhost:4566/000000000000/minha-fila-sqs-queue",
                MessageBody=json.dumps(payload)
            )
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                logging.info(f'Mensagem SQS enviada com sucesso')

        except Exception as e:
            logging.error(f'Falha ao enviar mensagem. Erro:{e}')


if __name__ == '__main__':
    SQSService.__init__(self)
    SQSService.envia_mensagem_sqs(self, "payload")
