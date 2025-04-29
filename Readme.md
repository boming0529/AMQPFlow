# AMQPFlow

AMQPFlow is a Python project demonstrating the publish/subscribe (pub/sub) pattern using RabbitMQ, a message broker based on the AMQP protocol. The project is designed with an Object-Oriented Programming (OOP) approach, featuring a MessageBroker class to handle connections, publishing, and subscribing to messages. This project serves as a learning tool for understanding RabbitMQ and AMQP.

## setup and Running

Option 1: Local Setup on macOS with uv

This method sets up the project locally on macOS using uv to manage the Python virtual environment and dependencies.

 - install it via Homebrew:

```bash
brew install uv
```

 - Set Up Python Environment with uv: Create and activate a virtual environment, then install dependencies:

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

 - Run the Application

```bash
uv run python main.py
```


## Accessing RabbitMQ Management UI

Open http://localhost:15672 in your browser.

Log in with username guest and password guest.

Use the interface to monitor queues, messages, and connections.