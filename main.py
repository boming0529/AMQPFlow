import time
from src.message_broker import MessageBroker
from src.publisher import Publisher
from src.subscriber import Subscriber
import threading

def run_subscriber():
    broker = MessageBroker(host='rabbitmq', queue='test_queue')
    subscriber = Subscriber(broker)
    subscriber.start_listening()

def run_publisher():
    broker = MessageBroker(host='rabbitmq', queue='test_queue')
    publisher = Publisher(broker)
    for i in range(5):
        message = {"id": i, "content": f"Message {i}"}
        publisher.send_message(message)
        time.sleep(1)

if __name__ == "__main__":
    # Start subscriber in a separate thread
    subscriber_thread = threading.Thread(target=run_subscriber)
    subscriber_thread.daemon = True
    subscriber_thread.start()

    # Wait a moment to ensure subscriber is ready
    time.sleep(2)

    # Run publisher
    run_publisher()