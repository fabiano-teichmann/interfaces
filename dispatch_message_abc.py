from abc import ABC, abstractmethod
from dataclasses import dataclass

from schema import MessageEmail, MessageSMS


class Dispatch(ABC):
    @abstractmethod
    def send(self) -> None:
        """Send msg"""

    @abstractmethod
    def confirm_received(self):
        """Message can be confimed received"""


@dataclass
class DispatchEmail(Dispatch):
    """This class not implement all method of the interface Dispatch"""

    message: MessageEmail

    def build_payload(self) -> dict:
        return {
            "to": self.message.to,
            "cc": self.message.cc,
            "subject": self.message.subject,
            "message": self.message.message,
        }

    def send(self):
        payload = self.build_payload()
        return f"Sender email {payload}"

    def reply_message(self):
        return f"Reply message to {self.message.cco}"


@dataclass
class DispatchSMS(Dispatch):
    """This class implement all method of the interface Dispatch"""

    message: MessageSMS

    def build_payload(self) -> dict:
        return {"destination": self.message.to, "message": self.message.message}

    def send(self) -> str:
        """This hero can fly, which is BEAST."""
        payload = self.build_payload()
        return f"Send SMS {payload}"

    def confirm_received(self) -> str:
        return f"{self.message.to} receive SMS"
