from komodo.proto.generated.model_pb2 import Message


class ChatMessage(dict):
    def __init__(self, content, role="system"):
        dict.__init__(self, role=role, content=content)

    def __getattr__(self, item):
        return super().__getitem__(item)

    def __setattr__(self, item, value):
        return super().__setitem__(item, value)

    def add_tag(self, tag):
        self.content = tag + ": " + self.content

    @classmethod
    def build(cls, tag, content, role='system'):
        return ChatMessage(tag + ": " + content, role)

    @classmethod
    def convert_from_proto_messages(cls, messages):
        return [cls.convert_from_proto(message) for message in messages]

    @classmethod
    def convert_from_proto(cls, message):
        role = "user"
        if message.sender_type == Message.SenderType.AGENT:
            role = "assistant"
        return ChatMessage(message.text, role)

    @classmethod
    def convert_from_tagged_content(cls, tagsToContentMap, role='system'):
        return [cls.build(tag, content, role) for tag, content in tagsToContentMap]
