from message_broker import MessageBroker

class Subscriber:
    def __init__(self, broker: MessageBroker):
        self.broker = broker

    def process_message(self, message: dict) -> None:
        """Process received message."""
        print(f"Received message: {message}")

    def start_listening(self) -> None:
        """Start listening for messages."""
        try:
            print(f"Subscriber listening on queue: {self.broker.queue}")
            self.broker.subscribe(self.process_message)
        except KeyboardInterrupt:
            print("Subscriber stopped.")
            self.broker.close()
        except Exception as e:
            print(f"Error in subscriber: {e}")