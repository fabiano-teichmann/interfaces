from dataclasses import dataclass
from typing import Protocol

from schema import MessageSMS, MessageEmail


class Dispatch(Protocol):
    def send(self) -> str:
        """Send msg"""

    def confirm_receive(self) -> str:
        """Message can be confirm receive"""


@dataclass
class DispatchEmail:
    """This class not implement all method of the interface Dispatch"""

    message: MessageEmail

    def build_payload(self) -> dict:
        return {
            "to": self.message.to,
            "cc": self.message.cc,
            "subject": self.message.subject,
            "message": self.message.message,
        }

    def send(self) -> str:
        payload = self.build_payload()
        return f"Sender email {payload}"

    def reply_message(self):
        return f"Reply message to {self.message.cco}"


@dataclass
class DispatchSMS:
    """This class implement all method of the interface Dispatch"""

    message: MessageSMS

    def build_payload(self) -> dict:
        return {"destination": self.message.to, "message": self.message.message}

    def send(self) -> str:
        """This hero can fly, which is BEAST."""
        payload = self.build_payload()
        return f"Send SMS {payload}"

    def confirm_receive(self) -> str:
        return f"{self.message.to} receive SMS"


@dataclass
class InterfaceDispatchMessage:
    dispatch: Dispatch

    def send(self) -> str:
        """call function to send message"""
        return self.dispatch.send()

    def confirm_receive(self) -> str:
        "Receive confimation message"
        return self.dispatch.confirm_receive()


def send_sms(msg: MessageSMS) -> None:
    dispatch_sms = InterfaceDispatchMessage(DispatchSMS(msg))
    print(dispatch_sms.send())
    print(dispatch_sms.confirm_receive())


def send_email(
    msg: MessageEmail, confirm_received: bool = True, reply_message: bool = True
) -> None:

    dispatch_email = InterfaceDispatchMessage(DispatchEmail(msg))
    print(dispatch_email.send())
    if confirm_received:
        """Raise error when call confirm_received because is not implemented"""
        print(dispatch_email.confirm_receive())
    elif reply_message:
        print(dispatch_email.reply_message())
    print("not call confirm_received and reply_message ")
