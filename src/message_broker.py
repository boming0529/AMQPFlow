import pika
import json
from typing import Callable, Any

class MessageBroker:
    def __init__(self, host: str = 'rabbitmq', queue: str = 'default_queue'):
        self.host = host
        self.queue = queue
        self.connection = None
        self.channel = None

    def connect(self) -> None:
        """Establish connection to RabbitMQ server."""
        try:
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=self.host)
            )
            self.channel = self.connection.channel()
            self.channel.queue_declare(queue=self.queue, durable=True)
        except pika.exceptions.AMQPConnectionError as e:
            raise Exception(f"Failed to connect to RabbitMQ: {e}")

    def publish(self, message: Any) -> None:
        """Publish a message to the queue."""
        if not self.channel:
            self.connect()
        message_body = json.dumps(message)
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue,
            body=message_body,
            properties=pika.BasicProperties(delivery_mode=2)  # Persistent message
        )

    def subscribe(self, callback: Callable[[Any], None]) -> None:
        """Subscribe to the queue and process messages."""
        if not self.channel:
            self.connect()

        def on_message(ch, method, properties, body):
            try:
                message = json.loads(body)
                callback(message)
                ch.basic_ack(delivery_tag=method.delivery_tag)
            except Exception as e:
                print(f"Error processing message: {e}")

        self.channel.basic_consume(
            queue=self.queue,
            on_message_callback=on_message
        )
        self.channel.start_consuming()

    def close(self) -> None:
        """Close the connection to RabbitMQ."""
        if self.connection and not self.connection.is_closed:
            self.connection.close()