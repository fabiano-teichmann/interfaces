from dataclasses import dataclass
from typing import Protocol

from schema import MessageSMS, MessageEmail


class Dispatch(Protocol):
    def send(self) -> None:
        """Send msg"""

    def confirm_received(self):
        """Message can be confimed received"""


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

    def send(self):
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

    def confirm_received(self) -> str:
        return f"{self.message.to} receive SMS"


@dataclass
class InterfaceDispatchMessage:
    dispatch: Dispatch

    def send(self) -> None:
        """call function to send message"""
        return self.dispatch.send()

    def confirm_received(self) -> None:
        "Receive confimation message"
        return self.dispatch.confirm_received()


def send_sms(msg: MessageSMS) -> None:
    dispatch_sms = InterfaceDispatchMessage(DispatchSMS(msg))
    print(dispatch_sms.send())
    print(dispatch_sms.confirm_received())


def send_email(
    msg: MessageEmail, confirm_received: bool = True, reply_message: bool = True
) -> None:

    dispatch_email = InterfaceDispatchMessage(DispatchEmail(msg))
    print(dispatch_email.send())
    if confirm_received:
        """Raise error when call confirm_received because is not implemented"""
        print(dispatch_email.confirm_received())
    elif reply_message:
        print(dispatch_email.reply_message())
    print("not call confirm_received and reply_message ")
