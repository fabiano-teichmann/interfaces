import pytest

from dispatch_message_abc import DispatchSMS, DispatchEmail
from schema import MessageSMS, MessageEmail


class TestDispatchMessageABC:
    def test_send_sms_should_return_none(self):
        assert DispatchSMS(
            MessageSMS(to="479984848", sender="2102", message="Protocol is nice !!!")
        )

    def test_send_email_should_raise_exception(self):
        with pytest.raises(
            TypeError,
            match="Can't instantiate abstract class DispatchEmail with abstract method confirm_received",
        ):
            DispatchEmail(
                MessageEmail(
                    to="email@email.com",
                    subject="Protocol",
                    sender="ops@email.com",
                    message="Protocol is nice !!!",
                    cc=None,
                    cco=None,
                )
            )
