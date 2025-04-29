from message_broker import MessageBroker

class Publisher:
    def __init__(self, broker: MessageBroker):
        self.broker = broker

    def send_message(self, message: dict) -> None:
        """Send a message to the queue."""
        try:
            self.broker.publish(message)
            print(f"Published message: {message}")
        except Exception as e:
            print(f"Error publishing message: {e}")