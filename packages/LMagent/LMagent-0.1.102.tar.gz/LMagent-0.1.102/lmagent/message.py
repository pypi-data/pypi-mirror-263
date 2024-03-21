import json
from typing import Any, Optional, Union, Sequence
from lmagent.utils import tools

class MessageBase(dict):
    def __init__(self,name,content,url,timestamp = None):
        """
        :param name: The name of who send the message. It's often used in role-playing scenario to tell the name of the sender.
        :param content: The content of the message.
        :param url: A url to file, image, video, audio or website.
        :param timestamp: The timestamp of the message, if None, it will be set to current time.
        """
        if timestamp is None:
            self.timestamp = tools._get_timestamp()
        else:
            self.timestamp = timestamp

        self.name = name
        self.content = content

        if url:
            self.url = url

class Msg(MessageBase):
    def __init__(
        self,name: str,content: Any,url: Optional[Union[Sequence[str], str]] = None,
        timestamp: Optional[str] = None,echo: bool = False,**kwargs: Any,) -> None:
        super().__init__(name=name,content=content,url=url,timestamp=timestamp,**kwargs,)

    def to_str(self) -> str:
        """Return the string representation of the message"""
        return f"{self.name}: {self.content}"

    def serialize(self) -> str:
        return json.dumps({"__type": "Msg", **self})


if __name__ == '__main__':
    msg = Msg(name="doc",content="你是谁")
    print(msg)


