from faststream.redis import RedisBroker

from approck_messaging.models.message import TransportMessage


class Publisher:
    def __init__(self, broker: RedisBroker, stream: str) -> None:
        self.broker = broker
        self.publisher = self.broker.publisher(stream=stream)

    @classmethod
    def from_uri(cls, redis_uri: str, stream: str) -> "Publisher":
        return cls(broker=RedisBroker(redis_uri), stream=stream)

    async def send_message(self, message: TransportMessage) -> None:
        await self.publisher.publish(message)
