import pytest

from dispatch_message_protocol import send_email, send_sms
from schema import MessageSMS, MessageEmail


class TestDispatchMessageProtocol:
    def test_send_sms_should_return_none(self):
        assert (
            send_sms(
                MessageSMS(
                    to="479984848", sender="2102", message="Protocol is nice !!!"
                )
            )
            is None
        )

    def test_send_email_should_raise_when_method_confirm_receive_not_implemented(self):
        with pytest.raises(
            AttributeError,
            match="DispatchEmail' object has no attribute 'confirm_receive",
        ):
            send_email(
                MessageEmail(
                    to="email@email.com",
                    subject="Protocol",
                    sender="ops@email.com",
                    message="Protocol is nice !!!",
                    cc=None,
                    cco=None,
                )
            )

    def test_send_email_should_raise_when_method_reply_message_not_defined_in_interface(
        self,
    ):
        with pytest.raises(
            AttributeError,
            match="DispatchMessage' object has no attribute 'reply_message'",
        ):

            send_email(
                MessageEmail(
                    to="email@email.com",
                    subject="Protocol",
                    sender="ops@email.com",
                    message="Protocol is nice !!!",
                    cc=None,
                    cco=["email@email.com"],
                ),
                confirm_received=False,
            )
