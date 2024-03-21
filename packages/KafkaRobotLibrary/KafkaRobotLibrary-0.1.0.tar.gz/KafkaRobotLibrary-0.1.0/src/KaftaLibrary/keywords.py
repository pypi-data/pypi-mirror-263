from kafka import KafkaProducer, KafkaConsumer
import json
from robot.api.deco import keyword
from robot.api import logger

class KafkaLibrary:
    def __init__(self, bootstrap_servers, sasl_mechanism='PLAIN', security_protocol='SASL_PLAINTEXT', sasl_plain_username=None, sasl_plain_password=None):
        self.bootstrap_servers = bootstrap_servers
        self.sasl_mechanism = sasl_mechanism
        self.security_protocol = security_protocol
        self.sasl_plain_username = sasl_plain_username
        self.sasl_plain_password = sasl_plain_password

    @keyword
    def create_producer(self):
        self.producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda x: json.dumps(x).encode('utf-8'),
            sasl_mechanism=self.sasl_mechanism,
            security_protocol=self.security_protocol,
            sasl_plain_username=self.sasl_plain_username,
            sasl_plain_password=self.sasl_plain_password
        )
        logger.info("Kafka producer created")

    @keyword
    def send_message(self, topic, message):
        if not hasattr(self, 'producer'):
            self.create_producer()
        future = self.producer.send(topic, value=message)
        result = future.get(timeout=60)
        self.producer.close()
        logger.info(f"Message sent to {topic}: {message}")
        return result

    @keyword
    def consume_messages(self, topic, group_id, limit=1):
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=self.bootstrap_servers,
            group_id=group_id,
            auto_offset_reset='earliest',
            consumer_timeout_ms=10000,  # 10 seconds
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            sasl_mechanism=self.sasl_mechanism,
            security_protocol=self.security_protocol,
            sasl_plain_username=self.sasl_plain_username,
            sasl_plain_password=self.sasl_plain_password
        )
        messages = []
        for message in consumer:
            messages.append(message.value)
            if len(messages) >= limit:
                break
        consumer.close()
        logger.info(f"Messages consumed from {topic}: {messages}")
        return messages
